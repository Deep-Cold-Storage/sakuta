from typing import List

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session
from ..database import get_db

from .. import models
from ..crud import crud_branches
from ..schemas import branches

router = APIRouter()


@router.get("/contractors/{contractor_id}/branches/", response_model=List[branches.Branch])
def read_branches(contractor_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_branches.get_branches(db=db, contractor_id=contractor_id, skip=skip, limit=limit, )


@router.post("/contractors/{contractor_id}/branches/", response_model=branches.Branch)
def create_branch(contractor_id: int, branch: branches.BaseBranch, db: Session = Depends(get_db)):
    try:
        return crud_branches.create_branch(db=db, branch=branch, contractor_id=contractor_id)
    except:
        return Response(status_code=400)


@router.delete("/contractors/{contractor_id}/branches/{branch_id}")
def delete_branch(contractor_id: int, branch_id: int, db: Session = Depends(get_db)):
    crud_branches.delete_branch(db=db, branch_id=branch_id)

    return Response(status_code=204)
