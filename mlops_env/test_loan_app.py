from loan_app import app
import pytest

# Test client that makes request to the application
# running the actual server

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    response = client.get("/")
    assert response.status_code == 200

def test_predictions(client):
    test_data = {
    "ApplicantIncome":1000000,
    "Credit_History":1.0,
    "Gender":"Male",
    "LoanAmount":120,
    "Married":"Yes"
    }

    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert response.json == {"loan_approval_status ": 'Approved'}
