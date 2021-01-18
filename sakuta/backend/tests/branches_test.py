import pytest


def test_post(client, contractor):
    json = {
        "name": "Test Branch",
        "address": "Podkarpacka 3",
        "country": "PL",
        "city": "Rzeszów"
    }

    response = client.post(f"/contractors/{contractor}/branches", json=json)
    data = response.json()

    assert response.status_code == 200


def test_patch(client, branch):
    json = {
        "name": "Better Branch Name"
    }

    branch_id = branch["branch_id"]
    contractor_id = branch["contractor_id"]

    response = client.patch(f"/branches/{branch_id}", json=json)
    assert response.status_code == 200


def test_delete(client, branch):
    branch_id = branch["branch_id"]

    response = client.delete(f"/branches/{branch_id}")

    assert response.status_code == 204
