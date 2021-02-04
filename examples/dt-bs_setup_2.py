import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)

class Address(Base):
    __tablename__ = 'address'
    street = Column(String(80), nullable=False)
    zip = Column(String(5), nullable=False)
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship(Employee)

engine = create_engine('sqlite:///employee_address.db')
Base.metadata.create_all(engine)