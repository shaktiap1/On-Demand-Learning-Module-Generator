import os, uuid, requests
from django.shortcuts import render
from django.conf import settings
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase
FIREBASE_CRED = os.getenv("FIREBASE_CRED_JSON", "serviceAccount.json")
cred = credentials.Certificate(FIREBASE_CRED)
initialize_app(cred)
db = firestore.client()

# Gemini settings
GEMINI_KEY = os.getenv("GEMINI_API_KEY", "<your_key>")
GEMINI_ENDPOINT = "https://api-inference.googleapis.com/v1/gemini:chat"

def call_gemini(prompt):
    headers = {"Authorization": f"Bearer {GEMINI_KEY}"}
    data = {"model": "gemini-pro", "messages": [{"role": "user", "content": prompt}]}
    resp = requests.post(GEMINI_ENDPOINT, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]

def module_form(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        audience = request.POST.get("audience", "beginner")
        prompt = f"Create a learning module on '{topic}' for a {audience}, including overview, objectives, concepts, and 5 MCQs."
        content = call_gemini(prompt)
        doc_id = str(uuid.uuid4())
        db.collection("modules").document(doc_id).set({
            "topic": topic,
            "audience": audience,
            "content": content
        })
        return render(request, "generator/module_form.html", {"content": content, "doc_id": doc_id})
    return render(request, "generator/module_form.html")
