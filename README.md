# 🚀 Python Day 11 — FastAPI Day 1

First day with FastAPI — built as part of my **#60DaysOfPython** challenge on **Day 11**.

---

## 📋 What This Project Covers

- FastAPI setup and project structure
- Creating GET routes
- Path parameters with automatic type validation
- Running a FastAPI app with Uvicorn
- Auto-generated Swagger UI (`/docs`)

---

## 🗂️ Routes

| Method | Endpoint           | Description        |
|--------|--------------------|--------------------|
| GET    | `/`                | Welcome message    |
| GET    | `/about`           | Developer info     |
| GET    | `/users/{user_id}` | Get user by ID     |
| GET    | `/health`          | API health status  |

---

## 🛠️ Technologies Used

- Python 3
- FastAPI
- Uvicorn

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/studyhaxer/python-day11-fastapi-day1.git
```

2. Navigate to the project folder:
```bash
cd python-day11-fastapi-day1
```

3. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install "fastapi[standard]"
```

5. Run the app:
```bash
uvicorn main:app --reload
```

6. Open in browser:
- API: `http://127.0.0.1:8000`
- Swagger Docs: `http://127.0.0.1:8000/docs`

---

## 📚 What I Learned

- How FastAPI works and why it is faster than Flask
- Difference between path parameters and query parameters
- How FastAPI auto-validates types using Python type hints
- Auto-generated API documentation with Swagger UI

---

## 👨‍💻 Author

**studyhaxer** — Day 11 of #60DaysOfPython | Day 1 of FastAPI 🚀
