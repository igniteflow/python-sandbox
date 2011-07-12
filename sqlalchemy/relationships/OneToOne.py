from sqlalchemy import *
from sqlalchemy.orm import *

metadata = MetaData()

parent_table = Table('parent', metadata,
    Column('id', Integer, primary_key=True)
)

child_table = Table('child', metadata,
    Column('id', Integer, primary_key=True),
    Column('parent_id', Integer, ForeignKey('parent.id'))
)

class Parent(object):
    pass

class Child(object):
    pass

mapper(Parent, parent_table, properties={
    'child': relationship(Child, uselist=False, backref='parent')
})

mapper(Child, child_table)