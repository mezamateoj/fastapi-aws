from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wiki Api. Call /search or /article or /summary"
    }


def test_get_search():
    response = client.get("/search/NBA")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_summary():
    response = client.get("/summary/NBA")
    assert response.status_code == 200
    assert len(response.json()) > 0
