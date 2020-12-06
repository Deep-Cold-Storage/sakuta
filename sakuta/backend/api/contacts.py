from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_contacts
from ..schemas import contacts

router = APIRouter()


@router.get("/contractors/{contractor_id}/contacts/", response_model=List[contacts.Contact])
def read_contacts(contractor_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_contacts.get_contacts(db=db, contractor_id=contractor_id, skip=skip, limit=limit)


@router.post("/contractors/{contractor_id}/contacts/", response_model=contacts.Contact)
def create_contact(contractor_id: int, contact: contacts.BaseContact, db: Session = Depends(get_db)):
    return crud_contacts.create_contact(db=db, contractor_id=contractor_id, contact=contact)


@router.delete("/contractors/{contractor_id}/contacts/{contact_id}")
def delete_contact(contractor_id: int, contact_id: int, db: Session = Depends(get_db)):
    crud_contacts.delete_contact(db=db, contact_id=contact_id)

    return Response(status_code=204)
