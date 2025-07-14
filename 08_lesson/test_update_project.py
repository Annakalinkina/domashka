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
        "name": "Project to Update",
        "description": "Description for update."
    }
    response = requests.post(BASE_URL, json=payload, headers=headers)
    return response.json().get("id")

def test_update_project_positive(headers, project_id):

    payload = {
        "name": "Updated Project",
        "description": "This project has been updated."
    }
    response = requests.put(f"{BASE_URL}/{project_id}", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json().get("name") == "Updated Project"

def test_update_project_negative(headers):

    payload = {
        "name": "Updated Project",
        "description": "This project has been updated."
    }
    response = requests.put(f"{BASE_URL}/wrong_id", json=payload, headers=headers)
    assert response.status_code == 404  #
    assert "error" in response.json()