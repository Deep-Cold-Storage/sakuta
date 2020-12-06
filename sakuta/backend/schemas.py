from pydantic import BaseModel
from typing import List, Optional


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


class Relation(BaseModel):
    relation_id: int
    contact_id: int
    branch_id: int

    class Config:
        orm_mode = True
