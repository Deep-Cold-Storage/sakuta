# pylint: disable=no-name-in-module
from pydantic import BaseModel
from typing import Optional


class BaseContact(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    description: Optional[str] = None


class Contact(BaseContact):
    contact_id: int
    contractor_id: int

    class Config:
        orm_mode = True
