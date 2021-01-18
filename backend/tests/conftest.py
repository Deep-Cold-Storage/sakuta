import pytest
from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base, get_db
from ..main import app


@pytest.fixture()
def client():
    engine = create_engine("sqlite:///./tests/test.db", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        yield TestingSessionLocal()

    app.dependency_overrides[get_db] = override_get_db

    client = TestClient(app)
    return client


# Create a new contractor, Returns ID
@pytest.fixture()
def contractor(client):
    json = {
        "name": "Black Mesa",
        "industry": "Science",
    }

    response = client.post("/contractors", json=json)
    return response.json()["contractor_id"]


# Create a new branch, Returns Object
@pytest.fixture()
def branch(client, contractor):
    json = {
        "name": "Test Branch",
        "address": "Podkarpacka 3",
        "country": "PL",
    }

    response = client.post(f"/contractors/{contractor}/branches", json=json)
    return response.json()


# Create a new contact, Returns Object
@pytest.fixture()
def contact(client, contractor):
    json = {
        "name": "Adam Mickiewicz",
        "email": "adam@bednarski.dev",
    }

    response = client.post(f"/contractors/{contractor}/contacts", json=json)
    return response.json()
