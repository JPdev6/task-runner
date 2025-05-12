from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from .worker import send_email_task
from fastapi.middleware.cors import CORSMiddleware



load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    recipient: str
    subject: str
    body: str

@app.post("/task/email")
def queue_email(request: EmailRequest) -> dict:
    result = send_email_task.delay(request.recipient, request.subject, request.body)
    return {"message": "✅ Queuing task to Celery...", "task_id": result.id}
