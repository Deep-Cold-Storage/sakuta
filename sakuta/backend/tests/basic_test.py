import pytest


def test_get_contractors(client):
    response = client.get("/contractors/")

    assert response.status_code == 200
    data = response.json()
