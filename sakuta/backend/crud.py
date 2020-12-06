from sqlalchemy.orm import Session
from . import models, schemas


# Contractors =======================================
def get_contractors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contractor).offset(skip).limit(limit).all()


def create_contractor(db: Session, contractor: schemas.Contractor):
    db_contractor = models.Contractor(**contractor.dict())

    db.add(db_contractor)
    db.commit()
    db.refresh(db_contractor)

    return db_contractor


def replace_contractor(db: Session, contractor: schemas.Contractor, contractor_id: int):
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


# Branches =======================================
def get_branches(contractor_id: int, db: Session, skip: int = 0, limit: int = 100):
    print(contractor_id)
    return db.query(models.Branch).filter(models.Branch.contractor_id == contractor_id).offset(skip).limit(limit).all()


def create_branch(db: Session, branch: schemas.Branch, contractor_id: int):
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

#   Contacts =======================================


def get_contacts(contractor_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).filter(models.Contact.contractor_id == contractor_id).offset(skip).limit(limit).all()


def create_contact(db: Session, contractor_id: int, contact: schemas.Contact):
    db_contact = models.Contact(**contact.dict())
    db.contact.contractor_id = contractor_id

    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)

    return db_contact


def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(models.Contact).filter(
        models.Contact.contact_id == contact_id).first()

    if not db_contact:
        return

    db.delete(db_contact)
    db.commit()
