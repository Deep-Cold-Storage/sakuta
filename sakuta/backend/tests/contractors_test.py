import pytest


def test_post(client):
    json = {
        "name": "Test McTest Face",
        "industry": "Artist",
        "description": "Test Contractor"
    }

    response = client.post("/contractors", json=json)

    assert response.status_code == 200
    assert response.json()["contractor_id"]


def test_get(client, contractor):
    response = client.get(f"/contractors/{contractor}")
    data = response.json()

    assert response.status_code == 200

    assert data["industry"] == "Science"


def test_patch(client, contractor):
    json = {
        "name": "Aparture Science"
    }

    response = client.patch(f"/contractors/{contractor}", json=json)
    assert response.status_code == 200

    # Check if a change was made.
    response = client.get(f"/contractors/{contractor}")
    data = response.json()

    assert data["name"] == "Aparture Science"
    assert data["industry"] == "Science"


def test_delete(client, contractor):
    response = client.delete(f"/contractors/{contractor}")

    assert response.status_code == 204
