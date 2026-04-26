# 🐛 FastAPI Issue Tracker

A simple Issue Tracker API built with **FastAPI** that allows you to create, read, update, and delete issues.
Data is stored locally in a JSON file for simplicity.

---

## 🚀 Features

* Create issues with title, description, and priority
* Retrieve all issues or a single issue by ID
* Update issue fields (partial updates supported)
* Delete issues
* Enum-based validation for status and priority
* Middleware to track request processing time
* CORS enabled for frontend integration

---

## 🗂️ Project Structure

```
.
├── app
│   ├── middleware
│   │   └── timer.py          # Request timing middleware
│   ├── routes
│   │   └── issues.py         # API endpoints
│   ├── schemas.py            # Pydantic models
│   └── storage.py            # JSON file storage logic
├── data
│   └── issues.json           # Local database
├── main.py                   # FastAPI app entry point
└── requirements.txt
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd Fast-Api-issue-tracker
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the server with:

```bash
fastapi dev main.py
```

App will be available at:

```
http://127.0.0.1:8000
```

---

## 📘 API Documentation

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```


---

## 📌 API Endpoints

### 🔹 Get all issues

```
GET /api/v1/issues/
```

### 🔹 Create an issue

```
POST /api/v1/issues/
```

**Body:**

```json
{
  "title": "Bug in login",
  "description": "Login fails with 500 error",
  "priority": "high"
}
```

---

### 🔹 Get a single issue

```
GET /api/v1/issues/{issue_id}
```

---

### 🔹 Update an issue

```
PUT /api/v1/issues/{issue_id}
```

---

### 🔹 Delete an issue

```
DELETE /api/v1/issues/{issue_id}
```

---

## 🧠 Data Model

### Issue

```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "priority": "low | medium | high",
  "status": "open | in_progress | closed"
}
```

---

## ⏱️ Middleware

Each request includes a response header:

```
X-Process-Time: <execution time>
```

This is added via custom middleware in:

```
app/middleware/timer.py
```

---

## 💾 Storage

* Data is stored in: `data/issues.json`
* No database required
* Uses simple file read/write operations

---

## ⚠️ Notes / Improvements

* Currently uses file-based storage (not suitable for production)
* No authentication or user management

---

## 🛠️ Future Enhancements

* Switch to a real database (SQLite / PostgreSQL)
* Add authentication (JWT)
* Add logging & error tracking

---

## 📄 License

This project is open-source and available for learning purposes.
