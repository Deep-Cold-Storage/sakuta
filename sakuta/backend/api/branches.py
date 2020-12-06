from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_branches
from ..schemas import branches

router = APIRouter()


@router.get("/contractors/{contractor_id}/branches/", response_model=List[branches.Branch], response_model_exclude_unset=True)
def get_branches(contractor_id: int, db: Session = Depends(get_db)):
    return crud_branches.get_branches(db=db, contractor_id=contractor_id)


@router.post("/contractors/{contractor_id}/branches/", response_model=branches.Branch, response_model_exclude_unset=True)
def create_branch(contractor_id: int, branch: branches.BaseBranch, db: Session = Depends(get_db)):
    try:
        return crud_branches.create_branch(db=db, branch=branch, contractor_id=contractor_id)
    except:
        return Response(status_code=400)


@router.put("/branches/{branch_id}", response_model=branches.Branch, response_model_exclude_unset=True)
def update_branch(branch_id: int, branch: branches.BaseBranch, db: Session = Depends(get_db)):
    try:
        return crud_branches.update_branch(db=db, branch=branch, branch_id=branch_id)
    except AttributeError:
        return Response(status_code=404)


@router.patch("/branches/{branch_id}", response_model=branches.Branch, response_model_exclude_unset=True)
def patch_branch(branch_id: int, branch: branches.BaseBranch, db: Session = Depends(get_db)):
    try:
        return crud_branches.patch_branch(db=db, branch=branch, branch_id=branch_id)
    except AttributeError:
        return Response(status_code=404)


@router.delete("/branches/{branch_id}")
def delete_branch(branch_id: int, db: Session = Depends(get_db)):
    crud_branches.delete_branch(db=db, branch_id=branch_id)

    return Response(status_code=204)
