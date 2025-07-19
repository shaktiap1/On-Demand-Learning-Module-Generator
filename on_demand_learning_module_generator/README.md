# 🧠 On-Demand Learning Module Generator

> Personalized AI-generated learning modules, built with Django, Firebase, GCP, and Gemini 1.5 Flash.

---

## 🚀 Overview

This project was developed under the mentorship of **Dr. Daya Shankar Sharma**.

It enables rapid, personalized learning content generation based on user goals and topics using **Gemini 1.5 Flash**, and refines future modules through real-time learner feedback.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **AI Model**: Gemini 1.5 Flash (prompt-engineered)
- **Database**: Google Firestore (via Firebase Admin SDK)
- **Deployment**: GCP App Engine + Docker
- **Infra**: Firebase rules, Dockerized CI/CD

---

## ✨ Key Features

✅ Generate structured learning modules (Theory + Code + Quizzes)  
✅ REST API: `POST /generate-module/`  
✅ Gemini API integration via mock service (easily swappable with real key)  
✅ Firestore for storing learner data and feedback  
✅ Docker-ready & GCP App Engine deployable  
✅ Feedback loop to simulate pseudo-RLHF fine-tuning

---

## 🔁 Sample API Workflow

**Endpoint:** `POST /generate-module/`  
**Request:**

```json
{
  "topic": "Linear Algebra",
  "level": "beginner",
  "goals": "visual understanding"
}
