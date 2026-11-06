import requests
from pypdf import PdfReader

with open("key.txt") as f:
    key = f.read().strip()

reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    text = text + page.extract_text()

question = input("Ask something about the PDF: ")

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"
headers = {"x-goog-api-key": key, "Content-Type": "application/json"}

prompt = "Answer using only this document. If the answer is not in it, say so.\n\nDocument:\n" + text + "\n\nQuestion: " + question
body = {"contents": [{"parts": [{"text": prompt}]}]}

response = requests.post(url, headers=headers, json=body, timeout=60)
print(response.status_code)

data = response.json()
answer = data["candidates"][0]["content"]["parts"][0]["text"]
print(answer)

with open("summary.txt", "w") as f:
    f.write(summary)# pdf-qa-bot
