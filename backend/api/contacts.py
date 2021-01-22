from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_contacts, crud_relations
from ..schemas import contacts

router = APIRouter()


@router.get("/contractors/{contractor_id}/contacts", response_model=List[contacts.Contact],  summary="Get all saved Contacts for this Contractor.")
def get_contacts(contractor_id: int, db=Depends(get_db)):
    return crud_contacts.get_contacts(db=db, contractor_id=contractor_id)


@router.post("/contractors/{contractor_id}/contacts", response_model=contacts.Contact, summary="Create a new Contact for this Contractor.")
def create_contact(contractor_id: int, contact: contacts.BaseContact, db=Depends(get_db)):
    return crud_contacts.create_contact(db=db, contractor_id=contractor_id, contact=contact)


@router.get("/contacts/{contact_id}", response_model=contacts.Contact,  summary="Get existing Contact by ID.")
def get_contact(contact_id: int, db=Depends(get_db)):
    contact = crud_contacts.get_contact(db=db, contact_id=contact_id)

    if contact is None:
        return Response(status_code=404)

    return contact


@router.put("/contacts/{contact_id}", response_model=contacts.Contact, summary="Replace existing Contact by ID.")
def update_contact(contact_id: int, contact: contacts.BaseContact, db=Depends(get_db)):
    try:
        return crud_contacts.update_contact(db=db, contact=contact, contact_id=contact_id)
    except AttributeError:
        return Response(status_code=404)


@router.patch("/contacts/{contact_id}", response_model=contacts.Contact, summary="Partially update Contact by ID.")
def patch_contact(contact_id: int, contact: contacts.BaseContact, db=Depends(get_db)):
    try:
        return crud_contacts.patch_contact(db=db, contact=contact, contact_id=contact_id)
    except AttributeError:
        return Response(status_code=404)


@router.delete("/contacts/{contact_id}", status_code=204, summary="Delete Contact by ID.")
def delete_contact(contact_id: int, db=Depends(get_db)):
    crud_contacts.delete_contact(db=db, contact_id=contact_id)

    return Response(status_code=204)


# New Solution
# Create contact with relation.

@router.get("/branches/{branch_id}/contacts", response_model=List[contacts.Contact],  summary="Get all Contacts for Branch by Branch ID.")
def get_contact_by_branch(branch_id: int, db=Depends(get_db)):

    relations = crud_relations.get_relations(db=db, branch_id=branch_id)
    contacts = []

    for item in relations:
        contact = crud_contacts.get_contact(db=db, contact_id=item.contact_id)
        contacts.append(contact)

    return contacts


@router.post("/contractors/{contractor_id}/branches/{branch_id}/contacts", response_model=contacts.Contact, summary="Create a new Contact and Relation with this Branch.")
def create_contact_by_branch(contractor_id: int, branch_id: int, contact: contacts.BaseContact, db=Depends(get_db)):
    contact = crud_contacts.create_contact(db=db, contractor_id=contractor_id, contact=contact)

    try:
        relation = crud_relations.create_relation_ids(db=db, contact_id=contact.contact_id, branch_id=branch_id)
    except:
        return Response(status_code=400)

    return contact


@router.post("/branches/{branch_id}/contacts/{contact_id}", summary="Create a relationship between existing contact and this Branch.")
def assign_contact_by_branch(branch_id: int, contact_id: int, db=Depends(get_db)):
    try:
        relation = crud_relations.create_relation_ids(db=db, contact_id=contact_id, branch_id=branch_id)
    except:
        return Response(status_code=400)

    return Response(status_code=204)


@router.delete("/branches/{branch_id}/contacts/{contact_id}", summary="Delete a relationship between existing contact and this Branch.")
def assign_contact_by_branch(branch_id: int, contact_id: int, db=Depends(get_db)):
    try:
        relation = crud_relations.delete_relation_ids(db=db, contact_id=contact_id, branch_id=branch_id)
    except:
        return Response(status_code=400)

    return Response(status_code=204)
