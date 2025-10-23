import requests
import pytest

BASE_URL = "https://reqres.in/api"
HEADERS = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}


def test_get_user():
    """Проверка получения пользователя"""
    response = requests.get(f"{BASE_URL}/users/2", headers=HEADERS)
    assert response.status_code == 200, "Статус код должен быть 200"

    data = response.json().get("data")
    assert data is not None, "Ответ должен содержать поле data"
    assert data["id"] == 2
    assert data["email"] == "janet.weaver@reqres.in"
    assert data["first_name"] == "Janet"
    assert data["last_name"] == "Weaver"


def test_create_user():
    """Проверка создания пользователя"""
    payload = {"name": "Mikhail", "job": "Tester"}
    response = requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    assert response.status_code == 201, "Статус код должен быть 201"
    data = response.json()
    assert data["name"] == "Mikhail"
    assert data["job"] == "Tester"
    assert "id" in data
    assert "createdAt" in data


def test_update_user():
    """Проверка обновления пользователя"""
    payload = {"name": "Alex", "job": "Engineer"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload, headers=HEADERS)

    assert response.status_code == 200, "Статус код должен быть 200"
    data = response.json()
    assert data["name"] == "Alex"
    assert data["job"] == "Engineer"
    assert "updatedAt" in data
