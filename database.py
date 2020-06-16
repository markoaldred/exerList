from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///test.db', echo=True)

class BaseMixin(object):
    @classmethod
    def add_item(cls, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()

class Checklist(BaseMixin, Base):
    __tablename__ = 'checklist'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    item_no = Column(Integer, nullable=False)
    
    tasks = relationship("Task", back_populates="checklist")
    
    def __repr__(self):
        return "<User(%r, %r)>" % (
            self.id, self.name)

class Task(BaseMixin, Base):
    __tablename__ = 'task'
    
    id = Column(Integer, primary_key=True)
    checklist_id = Column(Integer, ForeignKey('checklist.id'))
    description = Column(String, nullable=False)
    
    checklist = relationship("Checklist", back_populates="tasks")
    
    def __repr__(self):
        return "Task: %r" % self.description

class Tag(BaseMixin, Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('tag_parent.id'))
    name = Column(String, nullable=False)
    item_no = Column(Integer, nullable=False)

    tagparent = relationship("TagParent", back_populates="tags")

    def __repr__(self):
        return "Tag: %r" % self.name

class TagParent(BaseMixin, Base):
    __tablename__ = 'tag_parent'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    item_no = Column(Integer, nullable=False)

    tags = relationship("Tag", back_populates="tag_parent")

    def __repr__(self):
        return "Tag Type: %r" % self.name

class InstanceChecklist(BaseMixin, Base):
    __tablename__ = 'instance_checklist'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    checklist_id = Column(Integer, ForeignKey('checklist.id'))
    checklist_name = Column(String, nullable=False)
    document_no = Column(String, nullable=False)

    checklist = relationship("Checklist", back_populates="instance_checklist")
    instance_tasks = relationship("InstanceTask", back_populates="instance_checklist")

    def __repr__(self):
        return "Date: %s, Checklist Name: %s" % (date, checklist_name)

class InstanceTask(BaseMixin, Base):
    __tablename__ = 'instance_task'

    id = Column(Integer, primary_key=True)
    instance_checklist_id = Column(Integer, ForeignKey('instance_checklist.id'))
    task_name = Column(String, nullable=False)

    instance_checklist = relationship("InstanceChecklist", back_populates="instance_task")

    def __repr__(self):
        return "Instance Task: %s" % (task_name)

'''
class ChecklistTag(BaseMixin, Base):
    __tablename__ = 'checklist_tag'

    tag_id = Column(Integer, ForeignKey('tag.id'))
    checklist_id = Column(Integer, ForeignKey('checklist.id'))

    def __repr__(self):
        return "Tag: %s, Checklist: %s" % (tag_id, checklist_id)
'''

def build_db():
    global session
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    '''
    #Example of adding multiple items to database
    session.add_all([
        Checklist(item_no=0, name="LT Ciruculation Pump Calculation"),
        Checklist(item_no=1, name="Lube Oil PSV Calculation"),
        Checklist(item_no=2, name="HT PSV Calculation"),
        Checklist(item_no=3, name='Underground Drawing')
    ])
    session.commit()
    '''
#Create a list that links that data on the listbox to the database
def link_lstbox_db():
    linked_data = []
    for row in session.query(Checklist):
        d = {'id':row.id, 'name':row.name, 'item_no':row.item_no}
        linked_data.append(d)
    return linked_data

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



