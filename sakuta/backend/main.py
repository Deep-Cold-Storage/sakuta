from typing import List

from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/contractors/", response_model=List[schemas.Contractor])
def read_contractors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contractors = crud.get_contractors(db, skip=skip, limit=limit)
    return contractors


@app.post("/contractors/", response_model=schemas.Contractor)
def create_contractor(contractor: schemas.BaseContractor, db: Session = Depends(get_db)):
    return crud.create_contractor(db=db, contractor=contractor)


@app.put("/contractors/{contractor_id}", response_model=schemas.Contractor)
def replace_contractor(contractor_id: int, contractor: schemas.BaseContractor, db: Session = Depends(get_db)):
    return crud.replace_contractor(db=db, contractor=contractor, contractor_id=contractor_id)


@app.delete("/contractors/{contractor_id}")
def delete_contractor(contractor_id: int, db: Session = Depends(get_db)):
    crud.delete_contractor(db, contractor_id=contractor_id)

    return Response(status_code=204)


# Branches =======================================
@app.get("/contractors/{contractor_id}/branch/", response_model=List[schemas.Branch])
def read_branches(contractor_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_branches(db=db, contractor_id=contractor_id, skip=skip, limit=limit, )


@app.post("/contractors/{contractor_id}/branch/", response_model=schemas.Branch)
def create_branch(contractor_id: int, branch: schemas.BaseBranch, db: Session = Depends(get_db)):
    try:
        return crud.create_branch(db=db, branch=branch, contractor_id=contractor_id)
    except:
        return Response(status_code=400)


@app.delete("/contractors/{contractor_id}/branch/{branch_id}")
def delete_branch(contractor_id: int, branch_id: int, db: Session = Depends(get_db)):
    crud.delete_branch(db=db, branch_id=branch_id)

    return Response(status_code=204)


# CONTACT =======================================
@app.get("/contractors/{contractor_id}/contacts/", response_model=List[schemas.Contact])
def read_contacts(contractor_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_contacts(db=db, contractor_id=contractor_id, skip=skip, limit=limit)


@app.post("/contractors/{contractor_id}/contact/", response_model=schemas.Contact)
def create_contact(contractor_id: int, contact: schemas.BaseContact, db: Session = Depends(get_db)):
    return crud.create_contact(db=db, contractor_id=contractor_id, contact=contact)


@app.delete("/contractors/{contractor_id}/contact/{contact_id}")
def delete_contact(contractor_id: int, contact_id: int, db: Session = Depends(get_db)):
    crud.delete_contact(db=db, contractor_id=contractor_id,
                        contact_id=contact_id)

    return Response(status_code=204)
