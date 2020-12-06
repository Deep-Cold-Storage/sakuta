from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_contractors
from ..schemas import schema_contractors

router = APIRouter()


@router.get("/contractors/", response_model=List[schema_contractors.Contractor])
def read_contractors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contractors = crud_contractors.get_contractors(db, skip=skip, limit=limit)
    return contractors


@router.post("/contractors/", response_model=schema_contractors.Contractor)
def create_contractor(contractor: schema_contractors.BaseContractor, db: Session = Depends(get_db)):
    return crud_contractors.create_contractor(db=db, contractor=contractor)


@router.put("/contractors/{contractor_id}", response_model=schema_contractors.Contractor)
def replace_contractor(contractor_id: int, contractor: schema_contractors.BaseContractor, db: Session = Depends(get_db)):
    return crud_contractors.replace_contractor(db=db, contractor=contractor, contractor_id=contractor_id)


@router.delete("/contractors/{contractor_id}")
def delete_contractor(contractor_id: int, db: Session = Depends(get_db)):
    crud_contractors.delete_contractor(db, contractor_id=contractor_id)

    return Response(status_code=204)
