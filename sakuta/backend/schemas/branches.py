# pylint: disable=no-name-in-module
from pydantic import BaseModel
from typing import Optional


class BaseBranch(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None


class Branch(BaseBranch):
    branch_id: int
    contractor_id: int

    class Config:
        orm_mode = True
