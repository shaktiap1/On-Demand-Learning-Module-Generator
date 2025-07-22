# 🧠 On-Demand Learning Module Generator

Generate personalized learning content using Gemini + Django.

## 🛠 Stack

- Django backend (Python)
- Gemini API (Google)
- Firebase Firestore (for storage)
- Docker + gunicorn (production ready)

## 🚀 Getting Started

Clone the repo and install requirements:

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Set environment variables:

```bash
cp .env.example .env
# Then edit .env with real keys
```

Run the app:

```bash
python manage.py runserver
```

Or run via Docker:

```bash
docker build -t modulegen .
docker run -p 8000:8000 modulegen
```

Then open http://localhost:8000
