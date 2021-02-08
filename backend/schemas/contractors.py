# pylint: disable=no-name-in-module
from pydantic import BaseModel
from typing import Optional


class BaseContractor(BaseModel):
    name: Optional[str]
    industry: Optional[str]
    pesel: Optional[str]
    regon: Optional[str]
    nip: Optional[str]
    bank_account: Optional[str]
    bank_name: Optional[str]
    website: Optional[str]
    description: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Mickiewicz Inc.",
                "industry": "Artist",
                "nip": "6690506570",
                "website": "https://bednarski.dev",
                "description": "Very good deliverability! 8/10"
            }
        }


class Contractor(BaseContractor):
    contractor_id: int

    class Config:
        orm_mode = True


class BaseIntegrationContractor(BaseModel):
    name: Optional[str]
    nip: Optional[str]
    email: Optional[str]
    address: Optional[str]
    phone: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Mickiewicz Inc.",
                "nip": "6690506570",
                "email": "mickiewiczowny@gmail.com",
                "address": "Aleja Wlaclawa Kopisto",
                "phone": "+48885558084"
            }
        }


class IntegrationContractor(BaseIntegrationContractor):
    contractor_id: int

    class Config:
        orm_mode = True
