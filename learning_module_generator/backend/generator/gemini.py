import os
import requests

API_KEY = os.getenv('GEMINI_API_KEY')
GEN_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + API_KEY

def generate_learning_module(topic, level):
    prompt = f"""
You are an AI tutor. Generate a learning module for the topic "{topic}" suitable for a {level} learner. Include:
1. Title
2. Learning Objectives (3-5 bullet points)
3. Module Content (1-2 paragraphs)
4. 3 Multiple Choice Questions with answers
5. 2 External Resources (links)
"""
    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    r = requests.post(GEN_URL, json=body)
    r.raise_for_status()
    text = r.json()['candidates'][0]['content']['parts'][0]['text']
    return text
