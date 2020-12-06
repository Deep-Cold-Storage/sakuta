from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_contractors
from ..schemas import contractors

router = APIRouter()


@router.get("/contractors/", response_model=List[contractors.Contractor])
def get_contractors(db: Session = Depends(get_db)):
    return crud_contractors.get_contractors(db)


@router.post("/contractors/", response_model=contractors.Contractor)
def create_contractor(contractor: contractors.BaseContractor, db: Session = Depends(get_db)):
    return crud_contractors.create_contractor(db=db, contractor=contractor)


@router.put("/contractors/{contractor_id}", response_model=contractors.Contractor)
def update_contractor(contractor_id: int, contractor: contractors.BaseContractor, db: Session = Depends(get_db)):
    try:
        return crud_contractors.update_contractor(db=db, contractor=contractor, contractor_id=contractor_id)
    except AttributeError:
        return Response(status_code=404)


@router.patch("/contractors/{contractor_id}", response_model=contractors.Contractor)
def patch_contractor(contractor_id: int, contractor: contractors.BaseContractor, db: Session = Depends(get_db)):
    try:
        return crud_contractors.patch_contractor(db=db, contractor=contractor, contractor_id=contractor_id)
    except AttributeError:
        return Response(status_code=404)


@router.delete("/contractors/{contractor_id}")
def delete_contractor(contractor_id: int, db: Session = Depends(get_db)):
    crud_contractors.delete_contractor(db=db, contractor_id=contractor_id)

    return Response(status_code=204)
