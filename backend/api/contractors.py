from typing import List, Optional

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_contractors
from ..schemas import contractors

router = APIRouter()


@router.get("/contractors", response_model=List[contractors.Contractor], summary="Get all saved Contractors.")
def get_contractors(db=Depends(get_db), contractor_nip: Optional[str] = None):

    if contractor_nip:
        return crud_contractors.search_contractors_nip(db, contractor_nip)

    return crud_contractors.get_contractors(db)


@router.get("/contractors/{contractor_id}", response_model=contractors.Contractor, summary="Get Contractor by ID.")
def get_contractor(contractor_id: int, db=Depends(get_db)):
    contactor = crud_contractors.get_contractor(db=db, contractor_id=contractor_id)

    if not contactor:
        return Response(status_code=404)

    return contactor


@router.post("/contractors", response_model=contractors.Contractor, summary="Create a new Contractor.")
def create_contractor(contractor: contractors.BaseContractor, db=Depends(get_db)):
    return crud_contractors.create_contractor(db=db, contractor=contractor)


@router.put("/contractors/{contractor_id}", response_model=contractors.Contractor, summary="Replace existing Contractor by ID.")
def update_contractor(contractor_id: int, contractor: contractors.BaseContractor, db=Depends(get_db)):
    try:
        return crud_contractors.update_contractor(db=db, contractor=contractor, contractor_id=contractor_id)
    except AttributeError:
        return Response(status_code=404)


@router.patch("/contractors/{contractor_id}", response_model=contractors.Contractor, summary="Partially update Contractor by ID.")
def patch_contractor(contractor_id: int, contractor: contractors.BaseContractor, db=Depends(get_db)):
    try:
        return crud_contractors.patch_contractor(db=db, contractor=contractor, contractor_id=contractor_id)
    except AttributeError:
        return Response(status_code=404)


@router.delete("/contractors/{contractor_id}", status_code=204, summary="Delete Contractor by ID.")
def delete_contractor(contractor_id: int, db=Depends(get_db)):
    crud_contractors.delete_contractor(db=db, contractor_id=contractor_id)

    return Response(status_code=204)
