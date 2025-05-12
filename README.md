# 📬 FastAPI Background Task Runner with Celery & Redis

A clean and production-ready Python microservice built with FastAPI, Celery, Redis, and Docker. This project showcases background task execution for operations like sending emails, following best practices for structure, testing, and deployment.

---

## 🚀 Features

- ✅ FastAPI REST API with `/task/email` endpoint
- ✅ Celery background task queue
- ✅ Redis message broker
- ✅ Docker Compose for isolated dev environment
- ✅ Poetry dependency management
- ✅ `.env` support via `python-dotenv`
- ✅ Swagger UI (`/docs`) for testing
- ✅ Pytest for basic endpoint validation

---

## 🧱 Project Structure

```
task-runner/
├── src/
│   └── myapp/
│       ├── main.py           # FastAPI app
│       ├── worker.py         # Celery worker and task
│       └── __init__.py
├── tests/
│   └── test_task.py          # Pytest for POST /task/email
├── Dockerfile                # API container
├── docker-compose.yml        # Full stack (API + Celery + Redis)
├── .env                      # Local environment variables
├── pyproject.toml            # Poetry config
└── README.md
```

---

## ⚙️ Usage Instructions

### 🔧 1. Clone and Install

```bash
git clone https://github.com/YOUR_USERNAME/task-runner.git
cd task-runner
poetry install
```

### 🌐 2. Create a `.env` file

```env
REDIS_URL=redis://localhost:6379/0
```

> Needed for both FastAPI and Celery to connect to Redis.

---

### 🐳 3. Run with Docker

```bash
docker compose up --build
```

Access:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### ▶️ 4. Test Background Task

Send POST to `/task/email`:

```json
{
  "recipient": "test@example.com",
  "subject": "Hello",
  "body": "This is a test"
}
```

Watch logs for:

- ✅ `web-1` shows "Task queued..."
- ✅ `celery-1` shows "Processing task..."

---

### ✅ 5. Run Tests

```bash
poetry run pytest
```

---

## 🔍 Code Overview

### main.py

```python
@app.post("/task/email")
def queue_email(request: EmailRequest):
    print("✅ Queuing task...")
    result = send_email_task.delay(request.recipient, request.subject, request.body)
    print(f"✅ Task queued with ID: {result.id}")
    return {"message": "Email task queued"}
```

### worker.py

```python
@celery.task
def send_email_task(recipient: str, subject: str, body: str) -> str:
    print("📬 [Celery] Processing task...")
    print(f"To: {recipient} | Subject: {subject} | Body: {body}")
    return "Email sent"
```

---

## 🧪 Sample Test (tests/test_task.py)

```python
def test_queue_email():
    response = client.post("/task/email", json={
        "recipient": "test@example.com",
        "subject": "Hello",
        "body": "Test"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Email task queued"
```

---

## 🧠 Concepts Covered

- Background job queues
- Broker & task separation
- `.env`-based config loading
- Containerized microservices
- Async task offloading

---


---

## 📄 License

MIT