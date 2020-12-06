from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_contacts
from ..schemas import contacts

router = APIRouter()


@router.get("/contractors/{contractor_id}/contacts/", response_model=List[contacts.Contact], response_model_exclude_unset=True)
def get_contacts(contractor_id: int, db: Session = Depends(get_db)):
    return crud_contacts.get_contacts(db=db, contractor_id=contractor_id)


@router.post("/contractors/{contractor_id}/contacts/", response_model=contacts.Contact, response_model_exclude_unset=True)
def create_contact(contractor_id: int, contact: contacts.BaseContact, db: Session = Depends(get_db)):
    return crud_contacts.create_contact(db=db, contractor_id=contractor_id, contact=contact)


@router.put("/contacts/{contact_id}", response_model=contacts.Contact, response_model_exclude_unset=True)
def update_branch(contact_id: int, contacts: contacts.BaseContact, db: Session = Depends(get_db)):
    try:
        return crud_contacts.update_branch(db=db, contacts=contacts, contact_id=contact_id)
    except AttributeError:
        return Response(status_code=404)


@router.patch("/contacts/{contact_id}", response_model=contacts.Contact, response_model_exclude_unset=True)
def patch_branch(contact_id: int, contacts: contacts.BaseContact, db: Session = Depends(get_db)):
    try:
        return crud_contacts.patch_branch(db=db, contacts=contacts, contact_id=contact_id)
    except AttributeError:
        return Response(status_code=404)


@router.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    crud_contacts.delete_contact(db=db, contact_id=contact_id)

    return Response(status_code=204)
