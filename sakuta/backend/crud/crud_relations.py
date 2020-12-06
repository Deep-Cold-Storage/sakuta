from sqlalchemy.orm import Session

from .. import models
from ..schemas import relations


def get_relations(branch_id: int, db: Session):
    return db.query(models.Relation).filter(models.Relation.branch_id == branch_id).all()


def create_relation(db: Session, branch_id: int, relation: relations.Relation):
    db_relations = models.Relation(**relation.dict())
    db_relations.branch_id = branch_id

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
