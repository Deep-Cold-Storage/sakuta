from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_contractors, crud_branches, crud_contacts
from ..schemas import contractors

router = APIRouter()


@router.get("/integration", response_model=contractors.IntegrationContractor, summary="Get Contractor summary by NIP")
def get_integration(nip: str, db=Depends(get_db)):
    contractor = crud_contractors.search_contractors_nip(db, nip)
    if not contractor:
        return Response(status_code=404)

    contractor = contractor[0]

    contact = crud_contacts.get_contacts(db=db, contractor_id=contractor.contractor_id)

    if contact:
        contractor.phone = contact[0].phone
        contractor.email = contact[0].email

    branch = crud_branches.get_branches(db=db, contractor_id=contractor.contractor_id)

    if branch:
        contractor.address = branch[0].address

    return contractor
