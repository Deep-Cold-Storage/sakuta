from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_relations
from ..schemas import relations

router = APIRouter()


@router.get("/branches/{branch_id}/relations/", response_model=List[relations.Relation], response_model_exclude_unset=True)
def get_relations(branch_id: int, db: Session = Depends(get_db)):
    return crud_relations.get_relations(db=db, branch_id=branch_id)


@router.post("/branches/{branch_id}/relations/", response_model=relations.Relation, response_model_exclude_unset=True)
def create_relation(branch_id: int, relation: relations.BaseRelation, db: Session = Depends(get_db)):
    try:
        return crud_relations.create_relation(db=db, relation=relation, branch_id=branch_id)
    except:
        return Response(status_code=400)


@router.delete("/relation/{relation_id}")
def delete_relation(relation_id: int, db: Session = Depends(get_db)):
    crud_relations.delete_relation(db=db, relation_id=relation_id)

    return Response(status_code=204)