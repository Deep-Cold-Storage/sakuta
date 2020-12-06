from sqlalchemy.orm import Session

from .. import models
from ..schemas import branches


def get_branches(contractor_id: int, db: Session, skip: int = 0, limit: int = 100):
    print(contractor_id)
    return db.query(models.Branch).filter(models.Branch.contractor_id == contractor_id).offset(skip).limit(limit).all()


def create_branch(db: Session, branch: branches.Branch, contractor_id: int):
    db_branch = models.Branch(**branch.dict())
    db_branch.contractor_id = contractor_id

    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)

    return db_branch


def delete_branch(db: Session, branch_id: int):
    db_branch = db.query(models.Branch).filter(
        models.Branch.branch_id == branch_id).first()

    if not db_branch:
        return

    db.delete(db_branch)
    db.commit()
