from sqlalchemy.orm import Session

from .. import models
from ..schemas import relations


def get_relations(branch_id: int, db: Session):
    return db.query(models.Relation).filter(models.Relation.branch_id == branch_id).all()


def create_relation(db: Session, branch_id: int, relation: relations.Relation):
    db_relations = models.Relation(**relation.dict())
    db_relations.branch_id = branch_id

    # QUICK FIX! Check if used contact is assigned to the same contractor as a used branch, if not raise Exception.
    db_branch = db.query(models.Branch).filter(models.Branch.branch_id == branch_id).first()
    db_contact = db.query(models.Contact).filter(models.Contact.contact_id == relation.contact_id).first()

    if db_branch.contractor_id != db_contact.contractor_id:
        raise Exception

    db.add(db_relations)
    db.commit()
    db.refresh(db_relations)

    return db_relations


def create_relation_ids(db: Session, branch_id: int, contact_id: int):
    db_relations = models.Relation()
    db_relations.branch_id = branch_id
    db_relations.contact_id = contact_id

    # QUICK FIX! Check if used contact is assigned to the same contractor as a used branch, if not raise Exception.
    db_branch = db.query(models.Branch).filter(models.Branch.branch_id == branch_id).first()
    db_contact = db.query(models.Contact).filter(models.Contact.contact_id == contact_id).first()

    if db_branch.contractor_id != db_contact.contractor_id:
        raise Exception

    db.add(db_relations)
    db.commit()
    db.refresh(db_relations)

    return db_relations


def delete_relation(db: Session, relation_id: int):
    db_relation = db.query(models.Relation).filter(
        models.Relation.relation_id == relation_id).first()

    if not db_relation:
        return

    db.delete(db_relation)
    db.commit()


def delete_relation_ids(db: Session, branch_id: int, contact_id: int):
    db_relation = db.query(models.Relation).filter(
        models.Relation.branch_id == branch_id).filter(
        models.Relation.contact_id == contact_id).first()

    if not db_relation:
        return

    db.delete(db_relation)
    db.commit()
