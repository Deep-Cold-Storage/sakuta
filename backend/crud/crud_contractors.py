from sqlalchemy.orm import Session

from .. import models
from ..schemas import contractors


def get_contractors(db: Session):
    return db.query(models.Contractor).all()


def get_contractorsNIP(db: Session):
    return db.query(models.Contractor).all()


def get_contractor(db: Session, contractor_id: int):
    return db.query(models.Contractor).filter(models.Contractor.contractor_id == contractor_id).first()


def search_contractors_nip(db: Session, contractor_nip: str):
    return db.query(models.Contractor).filter(models.Contractor.nip == contractor_nip).all()


def create_contractor(db: Session, contractor: contractors.Contractor):
    db_contractor = models.Contractor(**contractor.dict())

    db.add(db_contractor)
    db.commit()
    db.refresh(db_contractor)

    return db_contractor


def update_contractor(db: Session, contractor: contractors.Contractor, contractor_id: int):
    db_contractor = db.query(models.Contractor).filter(
        models.Contractor.contractor_id == contractor_id).first()

    for key, value in contractor.dict().items():
        setattr(db_contractor, key, value)

    db.commit()
    db.refresh(db_contractor)

    return db_contractor


def patch_contractor(db: Session, contractor: contractors.Contractor, contractor_id: int):
    db_contractor = db.query(models.Contractor).filter(
        models.Contractor.contractor_id == contractor_id).first()

    for key, value in contractor.dict().items():
        if value:
            setattr(db_contractor, key, value)

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
