import requests

URL = "http://localhost:8080/api/v1/collections/default/documents"

with open("data/company_data.txt", "r") as f:
    lines = f.readlines()

documents = []

for i, line in enumerate(lines):
    if line.strip():
        documents.append({
            "id": str(i),
            "text": line.strip()
        })

response = requests.post(URL, json={"documents": documents})

print("STATUS:", response.status_code)
print("RESPONSE:", response.text)