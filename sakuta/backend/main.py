from typing import List

from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

from . import models
from .database import engine
from .api import contractors, branches, contacts

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contractors.router, tags=["Contractors"])
app.include_router(branches.router, tags=["Branches"])
app.include_router(contacts.router, tags=["Contacts"])
