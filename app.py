import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="AI Supervisor", layout="centered")

st.title("🤖 Enterprise AI Supervisor Chat")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask something about the company...")

def get_ai_response(query):
    query_lower = query.lower()

    try:
        if "best" in query_lower:
            res = requests.get(f"{BASE_URL}/best_performer").json()
            return f"🏆 Best performer is {res['best_employee']} with score {res['score']}"

        elif "under" in query_lower:
            res = requests.get(f"{BASE_URL}/underperformers").json()
            return f"⚠️ Underperformers: {res['underperformers']}"

        elif "strategy" in query_lower or "decision" in query_lower:
            res = requests.get(f"{BASE_URL}/strategy").json()
            return f"📊 Strategy: {res['strategy']} (Avg: {res['company_avg']})"

        elif "insight" in query_lower or "memory" in query_lower:
            res = requests.get(f"{BASE_URL}/insights").json()
            return f"🧠 Stored Insights: {res['stored_insights']}"

        elif "search" in query_lower or "find" in query_lower:
            res = requests.get(f"{BASE_URL}/search", params={"q": query}).json()
            results = res.get("results", [])

            if results:
                return "🔍 Related Insights:\n\n" + "\n".join(results)
            else:
                return "No related insights found."

        else:
            return "I can help with: best performer, underperformers, strategy, insights, or search."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Handle input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = get_ai_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(response)