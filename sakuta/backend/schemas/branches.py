# pylint: disable=no-name-in-module
from pydantic import BaseModel
from typing import Optional


class BaseBranch(BaseModel):
    name: Optional[str]
    address: Optional[str]
    postal_code: Optional[str]
    country: Optional[str]
    city: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Artistry - Rzeszów Branch",
                "address": "Podkarpacka 5/2",
                "postal_code": "37-700",
                "country": "PL",
                "city": "Rzeszów"
            }
        }


class Branch(BaseBranch):
    branch_id: int
    contractor_id: int

    class Config:
        orm_mode = True
