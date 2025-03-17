import requests

API_URL = "http://localhost:8000/ask"
question_data = {"question": "What is AI?"}

response = requests.post(API_URL, json=question_data)
print("Response:", response.json())
