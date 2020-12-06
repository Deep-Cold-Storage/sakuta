from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Contractor(Base):
    __tablename__ = "contractors"

    contractor_id = Column(Integer, primary_key=True,
                           index=True, autoincrement=True)
    name = Column(String)
    industry = Column(String)
    pesel = Column(String)
    regon = Column(String)
    nip = Column(String)
    bank_account = Column(String)
    bank_name = Column(String)
    website = Column(String)
    description = Column(String)

    
class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    contractor_id = Column(Integer, ForeignKey("contractors.contractor_id"))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    description = Column(String)


class Branch(Base):
    __tablename__ = "branches"

    branch_id = Column(Integer, primary_key=True,
                       index=True, autoincrement=True)
    contractor_id = Column(Integer, ForeignKey("contractors.contractor_id"))
    name = Column(String)
    address = Column(String)
    postal_code = Column(String)
    country = Column(String)
    city = Column(String)


class Relation(Base):
    __tablename__ = "relations"

    relations_id = Column(Integer, primary_key=True, index=True)
    contact_id = Column(Integer, ForeignKey("contacts.contact_id"))
    branch_id = Column(Integer, ForeignKey("branches.branch_id"))
