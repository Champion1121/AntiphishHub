
# Web-Based URL Phishing Detection & Cyber Security Awareness

This project is a full-stack web application for detecting phishing URLs and promoting cyber security awareness.

---

## 🧩 Project Structure

```
web_url_phishing_detection/
├── backend/
│   ├── app/
│   │   ├── main.py               # Flask application entry
│   │   ├── routes/               # Flask API routes (URL checker, admin, export)
│   │   ├── utils/                # Heuristic phishing detection logic
│   │   ├── models/               # SQLAlchemy models
├── frontend/
│   ├── src/components/App.js     # React app interface
│   ├── public/index.html
├── database/schema.sql           # Optional: SQL schema for MySQL setup
```

---

## 🚀 Features

- 🔗 **Phishing URL Detection**
- 🛡️ **Cyber Security Awareness Tips**
- 👤 **Admin Registration & Login**
- 📁 **CSV Export of Logs**
- 📱 **Mobile-friendly Interface**

---

## 🔧 Setup Instructions

### 1. ✅ Requirements

- Node.js + npm
- Python 3.8+
- MySQL (XAMPP or native install)

---

### 2. 🔙 Backend (Flask API)

#### Install Python packages

```bash
pip install flask flask-cors flask-sqlalchemy pymysql werkzeug
```

#### Setup MySQL (XAMPP)

- Start MySQL via XAMPP
- Create database: `phishing_db`

#### Run Flask

```bash
cd backend
python app/main.py
```

---

### 3. 🌐 Frontend (React)

```bash
cd frontend
npm install
npm start
```

Visit: [http://localhost:3000](http://localhost:3000)

---

## 🔐 Admin API

Register:

```http
POST /api/admin/register
{ "username": "admin", "password": "123456" }
```

Login:

```http
POST /api/admin/login
{ "username": "admin", "password": "123456" }
```

---

## 📤 Export URL Check Logs

[http://localhost:5000/api/export-logs](http://localhost:5000/api/export-logs) → CSV download

---

## 📌 Deployment Suggestions

- Use [Render.com](https://render.com) for Flask and React
- Or deploy to [Railway](https://railway.app) or VPS (Ubuntu + NGINX + Gunicorn)

Let me know if you want deployment help!
