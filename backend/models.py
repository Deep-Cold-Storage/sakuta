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

    branches = relationship("Branch", cascade="all, delete")
    contacts = relationship("Contact", cascade="all, delete")


class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True,
                        index=True, autoincrement=True)
    contractor_id = Column(Integer, ForeignKey("contractors.contractor_id"))
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    description = Column(String)

    relations = relationship("Relation", cascade="all, delete")


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

    relations = relationship("Relation", cascade="all, delete")


class Relation(Base):
    __tablename__ = "relations"

    relation_id = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    contact_id = Column(Integer, ForeignKey("contacts.contact_id"))
    branch_id = Column(Integer, ForeignKey("branches.branch_id"))
