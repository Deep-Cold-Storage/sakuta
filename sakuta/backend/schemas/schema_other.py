# pylint: disable=no-name-in-module
from pydantic import BaseModel


class Relation(BaseModel):
    relation_id: int
    contact_id: int
    branch_id: int

    class Config:
        orm_mode = True
