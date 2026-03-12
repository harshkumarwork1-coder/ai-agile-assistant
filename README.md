# ⚡ AI Agile Assistant
### Intelligent Sprint Planning & Risk Management System

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb)
![Groq AI](https://img.shields.io/badge/Groq_AI-Llama_3.3_70B-FF6B00?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?style=for-the-badge&logo=javascript)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🏎️ About The Project

**AI Agile Assistant** is a full stack, AI-powered Agile project management system built to automate sprint planning, predict project risks and analyze team workloads — all in seconds.

Inspired by the precision and speed of motorsport engineering, this tool is designed to help software teams move faster, plan smarter and deliver better results.

> Built independently as a Full Stack Development internship project by **Harsh Kumar**.

---

## 🚀 Live Features

| # | Feature | Endpoint |
|---|---------|----------|
| 01 | 🧠 AI Agile Plan Generator | `POST /project/create` |
| 02 | 📊 Dashboard Metrics | `GET /dashboard/{id}` |
| 03 | ✅ Task Tracker | `GET /task/{id}` |
| 04 | ⚠️ Risk Extractor | `GET /risk/{id}` |
| 05 | 👥 Workload Analyzer | `GET /workload/{id}` |
| 06 | 🔁 Sprint Retrospective | `GET /retrospective/{id}` |
| 07 | 📈 Sprint Analytics | `GET /analytics/{id}` |
| 08 | 🎯 AI Risk Predictor | `GET /risk-predictor/{id}` |
| 09 | 🔐 User Authentication | `POST /auth/register` `POST /auth/login` |
| 10 | 📁 Project Management | `POST /project/create` `GET /project/all` |

---

## 🛠️ Tech Stack

### Backend
- **Python** — Core programming language
- **FastAPI** — High performance REST API framework
- **MongoDB Atlas** — Cloud NoSQL database
- **Groq AI (Llama 3.3 70B)** — AI plan generation engine
- **JWT (python-jose)** — Token based authentication
- **Argon2** — Password hashing
- **PyMongo** — MongoDB driver

### Frontend
- **HTML5 / CSS3 / JavaScript (ES6)** — Pure frontend, no framework
- **Orbitron / Exo 2 / Share Tech Mono** — Google Fonts
- **Fetch API** — Backend communication
- **Motorsport Dark UI Theme** — Electric Blue + Silver design system

---

## 📁 Project Structure
```
AI-AGILE-ASSISTANT/
├── backend/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── project.py
│   │   ├── ai_routes.py
│   │   ├── dashboard_routes.py
│   │   ├── task_routes.py
│   │   ├── risk_routes.py
│   │   ├── workload_routes.py
│   │   ├── retrospective_routes.py
│   │   ├── analytics_routes.py
│   │   └── risk_predictor_routes.py
│   ├── services/
│   │   └── ai_services.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── .env.example
└── frontend/
    ├── index.html
    ├── register.html
    ├── login.html
    ├── welcome.html
    ├── dashboard.html
    ├── profile.html
    ├── about.html
    ├── css/
    │   ├── style.css
    │   ├── auth.css
    │   ├── welcome.css
    │   ├── dashboard.css
    │   ├── profile.css
    │   └── about.css
    └── js/
        ├── api.js
        └── main.js
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.11+
- MongoDB Atlas account
- Groq AI API key (free at [groq.com](https://groq.com))

### 1. Clone the repository
```bash
git clone https://github.com/harshkumarwork1-coder/ai-agile-assistant.git
cd ai-agile-assistant
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn pymongo python-jose passlib argon2-cffi python-dotenv groq
```

### 4. Configure environment variables
```bash
cd backend
cp .env.example .env
```

Edit `.env` with your credentials:
```
MONGO_URL=your_mongodb_atlas_url
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key
```

### 5. Start the backend
```bash
uvicorn main:app --reload
```

Backend runs at: `http://127.0.0.1:8000`  
API Docs at: `http://127.0.0.1:8000/docs`

### 6. Open the frontend
Open `frontend/index.html` in your browser directly.

---

## 🔐 API Authentication

All protected routes require a Bearer token in the header:
```
Authorization: Bearer <your_jwt_token>
```

Get your token by logging in via `POST /auth/login`.

---

## 🎨 UI Design System

| Element | Value |
|---------|-------|
| Primary Color | `#0095FF` (Electric Blue) |
| Secondary Color | `#C0C0C0` (Silver) |
| Background | `#080808` (Garage Black) |
| Accent Green | `#00FF88` |
| Accent Red | `#FF2200` |
| Display Font | Orbitron |
| Body Font | Exo 2 |
| Mono Font | Share Tech Mono |

---

## 👨‍💻 Developer

**Harsh Kumar**  
Full Stack Developer | AI Integration Enthusiast

- 🔗 [LinkedIn](https://linkedin.com/in/your-linkedin-here)
- 🐙 [GitHub](https://github.com/harshkumarwork1-coder)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">
  <strong>⚡ Built with speed, precision and passion — just like a race car. ⚡</strong>
</div>
