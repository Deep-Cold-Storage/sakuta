from sqlalchemy.orm import Session

from .. import models
from ..schemas import contractors


def get_contractors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contractor).offset(skip).limit(limit).all()


def create_contractor(db: Session, contractor: contractors.Contractor):
    db_contractor = models.Contractor(**contractor.dict())

    db.add(db_contractor)
    db.commit()
    db.refresh(db_contractor)

    return db_contractor


def replace_contractor(db: Session, contractor: contractors.Contractor, contractor_id: int):
    db_contractor = db.query(models.Contractor).filter(
        models.Contractor.contractor_id == contractor_id).update(**contractor.dict())

    db.commit()
    db.refresh(db_contractor)

    return db_contractor


def delete_contractor(db: Session, contractor_id: int):
    db_contractor = db.query(models.Contractor).filter(
        models.Contractor.contractor_id == contractor_id).first()

    if not db_contractor:
        return

    db.delete(db_contractor)
    db.commit()
