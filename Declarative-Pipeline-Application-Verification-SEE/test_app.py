import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_response_body(client):
    response = client.get("/")

    expected_response = {
        "message": "Welcome to the Flask CI/CD Application",
        "status": "success"
    }

    assert response.get_json() == expected_response