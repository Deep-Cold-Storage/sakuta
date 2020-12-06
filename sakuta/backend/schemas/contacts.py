# pylint: disable=no-name-in-module
from pydantic import BaseModel
from typing import Optional


class BaseContact(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Adam Mickiewicz",
                "email": "adam@bednarski.dev",
                "description": "A very funny guy!"
            }
        }


class Contact(BaseContact):
    contact_id: int
    contractor_id: int

    class Config:
        orm_mode = True
