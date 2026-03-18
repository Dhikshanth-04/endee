from fastapi import FastAPI
from analyzer import get_best_employee, get_underperformers, get_strategy
from endee_client import search_insights

app = FastAPI(title="AI Supervisor with Endee 🚀")

@app.get("/")
def home():
    return {"message": "System Running with Endee ✅"}

@app.get("/best_performer")
def best():
    return get_best_employee()

@app.get("/underperformers")
def low():
    return get_underperformers()

@app.get("/strategy")
def strategy():
    return get_strategy()

@app.get("/search")
def search(q: str):
    return {
        "results": search_insights(q)
    }
