import os
import sentry_sdk
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from . import models
from .database import engine
from .api import contractors, branches, contacts, relations

models.Base.metadata.create_all(bind=engine)

sentry_sdk.init(
    "https://31fdd0a4edc549279455489370272db3@o352799.ingest.sentry.io/5626762",
    traces_sample_rate=1.0
)

tags_metadata = [
    {
        "name": "Contractors",
        "description": "Operations with Contractors. Create, edit, and replace contractors. This is the most important object and **should be created first.**",
    },
    {
        "name": "Branches",
        "description": "Operations with Branches for **existing** contractors. Create, edit, and delete branches.",
    },
    {
        "name": "Contacts",
        "description": "Operations with Contacts for **existing** contractors. Create, edit, and delete contacts.",
    },
    {
        "name": "Relations",
        "description": "Operations with Relations for **existing** branches and contacts. Create and delete relations between **existing** contacts and branches.",
    }
]

app = FastAPI(root_path=os.getenv("ROOT_PATH"), servers=[
    {"url": "http://127.0.0.1:5000", "description": "Development Environment"},
    {"url": "https://sakuta.bednarski.dev", "description": "Production Environment"},
])


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
        tags=tags_metadata,

    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
