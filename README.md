
# 📘 Full-Stack Coding Assignment – HRMS Lite

## Human Resource Management System

### 👨‍💻 Author

**Virendra Kumar Verma**

---

## 📌 Project Overview

* **Frontend:** Interactive React UI with modular folder structure.
* **Backend:** High-performance FastAPI (Python).
* **Database:** Robust PostgreSQL persistence.
* **ORM:** SQLAlchemy for efficient database modeling.

---

## 🛠️ Tech Stack

| Layer | Technology |
| --- | --- |
| **Frontend** | React 18, Vite, Tailwind CSS |
| **Backend** | **Python 3.10+, FastAPI** |
| **Database** | PostgreSQL |
| **ORM** | **SQLAlchemy** |
| **Validation** | **Pydantic Models** |

---

## 📁 Project Structure (Updated)

```text
hrms-lite/
├── frontend/             # React Frontend
│   ├── src/
│   │   ├── components/  # Reusable UI elements (Buttons, Inputs)
│   │   ├── pages/       # Full pages (Dashboard, EmployeeList)
│   │   ├── hooks/       # Custom React hooks (useFetch, etc.)
│   │   ├── services/    # API calling logic (Axios/Fetch)
│   │   └── index.css    # Global styles & Tailwind
│   └── package.json
│
├── backend/              # Python FastAPI Backend
│   ├── main.py          # Entry point & App initialization
│   ├── database.py      # SQLAlchemy Connection & Session logic
│   ├── models.py        # Database Schema & Relationships
│   ├── routers/         # API Route Modules
│   │   ├── employee.py
│   │   ├── attendance.py
│   │   └── dashboard.py
│   └── requirements.txt  # Python Dependencies
│
└── README.md

```

---

## 💻 Installation & Setup

### 🎨 Frontend Setup (React)

1. **Navigate to frontend folder:**
```bash
cd frontend

```


2. **Install dependencies:**
```bash
npm install

```


3. **Connect to Python Backend:**
Apne `services/` folder mein API base URL ko badal kar ye karein:
`http://localhost:8000`
4. **Start frontend server:**
```bash
npm run dev

```



### 🔧 Backend Setup (Python)

1. **Navigate to backend folder:**
```bash
cd backend

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Start FastAPI Server:**
```bash
uvicorn main:app --reload

```



---

## 📚 API Endpoints Summary

* **Dashboard:** `GET /dashboard` - Real-time HR statistics.
* **Employees:** `GET /employees`, `POST /employees`, `DELETE /employees/{id}`.
* **Attendance:** `GET /attendance`, `POST /attendance`, `GET /attendance/today`.

---

## ⚠️ Important Migration Note

Pehle ye project Node.js (Port 5000) par chalta tha. Migration ke baad, ab backend **Port 8000** par run hota hai. Frontend ke `services/` folder mein saare API calls ko naye port par map kar diya gaya hai.

---

### 🚀 Final Note

Yeh project meri adaptability dikhata hai ki kaise main **JavaScript (Node.js)** aur **Python (FastAPI)** dono environment mein production-grade code likh sakta hoon.

---

### Virendra bhai, ek choti si advice:

Aapka frontend structure bahut achha hai, lekin ek cheez check kar lena:

> Aapke `frontend/src/services/` folder ke andar jo file hai (shayad `api.js` ya `employeeService.js`), usmein purana port `5000` likha hoga. Use badal kar **`8000`** zaroor kar dena, nahi to frontend data load nahi karega.

**Kya aap chahte hain ki main aapke `services/` folder ke liye ek sample Python-compatible API file likh kar doon?** Would you like me to help with anything else?