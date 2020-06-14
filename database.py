from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite://', echo=True)

class Checklist(Base):
    __tablename__ = 'checklist'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    tasks = relationship("Task", back_populates="checklist")
    
    def __repr__(self):
        return "<User(%r, %r)>" % (
            self.id, self.name)
    
class Task(Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True)
    checklist_id = Column(Integer, ForeignKey('checklist.id'))
    description = Column(String, nullable=False)
    
    checklist = relationship("Checklist", back_populates="tasks")
    
    def __repr__(self):
        return "Task: %r" % self.description

def build_db():
    global session
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    #Example of adding multiple items to database
    session.add_all([
        Checklist(name="LT Ciruculation Pump Calculation"),
        Checklist(name="Lube Oil PSV Calculation"),
        Checklist(name="HT PSV Calculation"),
        Checklist(name='Underground Drawing')
    ])
    session.commit()

#Create a list that links that data on the listbox to the database
def link_lstbox_db():
    linked_data = []
    listbox_item = 0
    for row in session.query(Checklist):
        d = {'listbox_item':listbox_item, 'id':row.id, 'name':row.name}
        linked_data.append(d)
        listbox_item += 1
    return linked_data
    #print(linked_data)

'''
#Example of adding Items to checklist
new_checklist = Checklist(name="HT Circulation Pump Calculation")
session.add(new_checklist)
session.commit()

#Example of querying the entered information
query = session.query(Checklist).all()
print(query)

#Example of iterating thorugh the query results
for row in session.query(Checklist, Checklist.name):
    print(row.Checklist, row.name)
'''



