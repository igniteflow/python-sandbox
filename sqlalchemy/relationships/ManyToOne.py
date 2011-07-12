from sqlalchemy import *
from sqlalchemy.orm import *

metadata = MetaData()

parent_table = Table('parent', metadata,
    Column('id', Integer, primary_key=True),
    Column('child_id', Integer, ForeignKey('child.id')))

child_table = Table('child', metadata,
    Column('id', Integer, primary_key=True),
    )

class Parent(object):
    pass

class Child(object):
    pass

mapper(Parent, parent_table, properties={
    'child': relationship(Child)
})

''' 
alternatively implementation
mapper(Parent, parent_table, properties={
    'child': relationship(Child, backref="parents")
})
'''

mapper(Child, child_table)

print mapper