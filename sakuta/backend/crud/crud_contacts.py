from sqlalchemy.orm import Session

from .. import models
from ..schemas import contacts


def get_contacts(contractor_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).filter(models.Contact.contractor_id == contractor_id).offset(skip).limit(limit).all()


def create_contact(db: Session, contractor_id: int, contact: contacts.Contact):
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
