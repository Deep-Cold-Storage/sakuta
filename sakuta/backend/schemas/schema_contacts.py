# pylint: disable=no-name-in-module
from pydantic import BaseModel
from typing import Optional


class BaseContact(BaseModel):
    name: str
    email: str
    phone: str
    description: Optional[str] = None


class Contact(BaseContact):
    contact_id: int
    contractor_id: int

    class Config:
        orm_mode = True
