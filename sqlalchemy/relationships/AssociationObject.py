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
    Column('left_id', Integer, ForeignKey('left.id'), primary_key=True),
    Column('right_id', Integer, ForeignKey('right.id'), primary_key=True),
    Column('data', String(50))
)

class Parent(object):
    pass

class Child(object):
    pass

class Association(object):
    pass

mapper(Parent, left_table, properties={
    'children':relationship(Association)
})

mapper(Association, association_table, properties={
    'child':relationship(Child)
})

mapper(Child, right_table)

'''
# bidirection adds backrefs

mapper(Parent, left_table, properties={
    'children':relationship(Association, backref="parent")
})

mapper(Association, association_table, properties={
    'child':relationship(Child, backref="parent_assocs")
})

mapper(Child, right_table)
'''