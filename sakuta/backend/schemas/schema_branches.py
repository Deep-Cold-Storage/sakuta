# pylint: disable=no-name-in-module
from pydantic import BaseModel


class BaseBranch(BaseModel):
    name: str
    address: str
    postal_code: str
    country: str
    city: str


class Branch(BaseBranch):
    branch_id: int
    contractor_id: int

    class Config:
        orm_mode = True
