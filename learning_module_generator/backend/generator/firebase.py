import os
import firebase_admin
from firebase_admin import credentials, firestore
import datetime

# Initialize Firebase app once
cred_path = os.getenv('FIREBASE_CRED_JSON', 'firebase_credentials.json')
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
db = firestore.client()

def save_module(user_id, topic, module_text):
    doc = {
        "user": user_id,
        "topic": topic,
        "module": module_text,
        "timestamp": datetime.datetime.utcnow()
    }
    db.collection("modules").add(doc)
