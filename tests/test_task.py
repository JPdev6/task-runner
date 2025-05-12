from fastapi.testclient import TestClient

from myapp.main import app

client = TestClient(app)


def test_queue_email():
    response = client.post("/task/email", json={
        "recipient": "test@example.com",
        "subject": "Hello",
        "body": "This is a test"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Email task queued"}
