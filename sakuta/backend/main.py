from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from . import models
from .database import engine
from .api import contractors, branches, contacts, relations

models.Base.metadata.create_all(bind=engine)


tags_metadata = [
    {
        "name": "Contractors",
        "description": "Operations with Contractors. Create, edit, and replace contractors. This is the most important object and **should be created first.**",
    },
    {
        "name": "Branches",
        "description": "Operations with Branches for existing contractors. Create, edit, and delete branches.",
    },
    {
        "name": "Contacts",
        "description": "Operations with Contacts for existing contractors. Create, edit, and delete contacts.",
    },
    {
        "name": "Relations",
        "description": "Operations with Relations for existing branches and contacts. Create and delete relations between **existing** contacts and branches.",
    }
]

app = FastAPI()


app.include_router(contractors.router, tags=["Contractors"])
app.include_router(branches.router, tags=["Branches"])
app.include_router(contacts.router, tags=["Contacts"])
app.include_router(relations.router, tags=["Relations"])


def custom_openapi():
    openapi_schema = get_openapi(
        title="Sakuta - Backend",
        version="0.5.1",
        description="This page contacts the latest auto-generated OpenAPI specification for our contractor management module. 🔥 Enjoy the power of Python FastAPI!",
        routes=app.routes,
        tags=tags_metadata
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
