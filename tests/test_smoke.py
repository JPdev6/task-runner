from fastapi.testclient import TestClient

from myapp.main import app

client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to MyApp – your FastAPI project is running!"
    }
