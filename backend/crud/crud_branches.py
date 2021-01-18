from sqlalchemy.orm import Session

from .. import models
from ..schemas import branches


def get_branches(contractor_id: int, db: Session):
    return db.query(models.Branch).filter(models.Branch.contractor_id == contractor_id).all()


def create_branch(db: Session, branch: branches.Branch, contractor_id: int):
    db_branch = models.Branch(**branch.dict())
    db_branch.contractor_id = contractor_id

    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)

    return db_branch


def update_branch(db: Session, branch: branches.Branch, branch_id: int):
    db_branch = db.query(models.Branch).filter(
        models.Branch.branch_id == branch_id).first()

    for key, value in branch.dict().items():
        setattr(db_branch, key, value)

    db.commit()
    db.refresh(db_branch)

    return db_branch


def patch_branch(db: Session, branch: branches.Branch, branch_id: int):
    db_branch = db.query(models.Branch).filter(
        models.Branch.branch_id == branch_id).first()

    for key, value in branch.dict().items():
        if value:
            setattr(db_branch, key, value)

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
