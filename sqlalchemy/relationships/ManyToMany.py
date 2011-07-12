from sqlalchemy import *
from sqlalchemy.orm import *

metadata = MetaData()


left_table = Table('left', metadata,
    Column('id', Integer, primary_key=True)
)

right_table = Table('right', metadata,
    Column('id', Integer, primary_key=True)
)

association_table = Table('association', metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(object):
    pass

class Child(object):
    pass

mapper(Parent, left_table, properties={
    'children': relationship(Child, secondary=association_table)
})

mapper(Child, right_table)