from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {
        "message": "Iris Prediction API is running"
    }
    
def test_prediction():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    
    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1, 2]