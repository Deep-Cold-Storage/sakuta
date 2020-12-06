# pylint: disable=no-name-in-module
from pydantic import BaseModel
from typing import Optional


class BaseContractor(BaseModel):
    name: str
    industry: Optional[str] = None
    pesel: Optional[str] = None
    regon: Optional[str] = None
    nip: Optional[str] = None
    bank_account: Optional[str] = None
    bank_name: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None


class Contractor(BaseContractor):
    contractor_id: int

    class Config:
        orm_mode = True
