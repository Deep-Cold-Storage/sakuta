import pytest


def test_post(client, contractor):
    json = {
        "name": "Adam Mickiewicz",
        "email": "adam@bednarski.dev",
        "description": "A very funny guy!"
    }

    response = client.post(f"/contractors/{contractor}/contacts", json=json)
    data = response.json()

    assert response.status_code == 200


def test_patch(client, contact):
    json = {
        "name": "Better Adam Mickiewicz",
    }

    contact_id = contact["contact_id"]
    contractor_id = contact["contractor_id"]

    response = client.patch(f"/contacts/{contact_id}", json=json)
    assert response.status_code == 200


def test_delete(client, contact):
    contact_id = contact["contact_id"]

    response = client.delete(f"/contacts/{contact_id}")

    assert response.status_code == 204
