import requests

d = {"1": (False, "question")}

response = requests.get("https://stefanvasak.pythonanywhere.com/")
response2 = requests.post("https://stefanvasak.pythonanywhere.com/upload", json=d)

print(response.json())
print(response2.text)


POST https://us-central1-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/text-bison:predict