# pylint: disable=no-name-in-module
from pydantic import BaseModel


class BaseRelation(BaseModel):
    contact_id: int

    class Config:
        orm_mode = True


class Relation(BaseRelation):
    relation_id: int
    branch_id: int
