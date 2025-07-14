import requests
import pytest

BASE_URL = "http://example.com/api-v2/projects"  # Заменить на реальный базовый URL

@pytest.fixture
def headers():
    return {
        "Authorization": "Bearer YOUR_TOKEN"  # Замените на ваш токен
    }

def test_create_project_positive(headers):
    
    payload = {
        "name": "Test Project",
        "description": "This is a test project."
    }
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()

def test_create_project_negative(headers):

    payload = {
        "description": "This is a test project without a name."
    }
    response = requests.post(BASE_URL, json=payload, headers=headers)
    assert response.status_code == 400
    assert "error" in response.json()