import requests
import pytest

BASE_URL = "http://example.com/api-v2/projects"  # Заменить на реальный базовый URL

@pytest.fixture
def headers():
    return {
        "Authorization": "Bearer YOUR_TOKEN"  # Замените на ваш токен
    }

@pytest.fixture
def project_id(headers):

    payload = {
        "name": "Project for Get",
        "description": "Description for get."
    }
    response = requests.post(BASE_URL, json=payload, headers=headers)
    return response.json().get("id")

def test_get_project_positive(headers, project_id):

    response = requests.get(f"{BASE_URL}/{project_id}", headers=headers)
    assert response.status_code == 200
    assert response.json().get("id") == project_id

def test_get_project_negative(headers):

    response = requests.get(f"{BASE_URL}/wrong_id", headers=headers)
    assert response.status_code == 404
    assert "error" in response.json()