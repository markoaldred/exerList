from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite://', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship

class Department(Base):
   __tablename__ = 'department'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   employees = relationship('Employee', secondary = 'link')
   
class Employee(Base):
   __tablename__ = 'employee'
   id = Column(Integer, primary_key = True)
   name = Column(String)
   departments = relationship(Department,secondary='link')

class Link(Base):
   	__tablename__ = 'link'
   	department_id = Column(Integer, ForeignKey('department.id'), primary_key = True)
   	employee_id = Column(Integer, ForeignKey('employee.id'), primary_key = True)