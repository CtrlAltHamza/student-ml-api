from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_prediction_endpoint() -> None:
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    assert response.json() == {"input": 10, "prediction": 20}


def test_prediction_requires_value() -> None:
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_prediction_rejects_invalid_value() -> None:
    response = client.post("/predict", json={"value": "not-a-number"})
    assert response.status_code == 422