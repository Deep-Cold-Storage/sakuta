from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from . import models
from .database import engine
from .api import contractors, branches, contacts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contractors.router, tags=["Contractors"])
app.include_router(branches.router, tags=["Branches"])
app.include_router(contacts.router, tags=["Contacts"])


def custom_openapi():
    openapi_schema = get_openapi(
        title="Sakuta - Backend",
        version="0.5.1",
        description="This page contacts the latest auto-generated OpenAPI specification for our contractor management module. 🔥 Enjoy the power of Python FastAPI!",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
