from celery import Celery
import os
from dotenv import load_dotenv
from celery import shared_task

load_dotenv()

celery_app = Celery(
    "myapp",
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),  # ✅ fallback default
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0")
)

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery = Celery(
    "worker",
    broker=redis_url,
    backend=redis_url
)

@shared_task
def send_email_task(recipient: str, subject: str, body: str) -> str:
    print("📬 [Celery] Processing task...")
    print(f"To: {recipient} | Subject: {subject} | Body: {body}")
    return "Email sent"