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
