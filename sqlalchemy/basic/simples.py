# notes from from http://www.sqlalchemy.org/docs/orm/tutorial.html

# establish database connection
from sqlalchemy import create_engine

DB_ENGINE = 'mysql://root:root@localhost/Sandbox__sqlalchemy'
engine = create_engine(DB_ENGINE, echo=True)

# create a mysql table
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()
users_table = Table('users', metadata,
   Column('id', Integer, primary_key=True),
   Column('name', String(50)),
   Column('fullname', String(50)),
   Column('password', String(12))
)

metadata.create_all(engine)


# now add a python class 
class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)
    
# associate the table and class using SQLAlchemy's Mapper
from sqlalchemy.orm import mapper
mapper(User, users_table)

# create and inspect a user object
jimi = User('Jimi', 'Jimi Hendrix', 'password')
print jimi.name
print jimi.fullname
print jimi.password

# create a session to communicate with the database.
# use the session to write jimi to the db 
from sqlalchemy.orm import sessionmaker

# create a Session Factory which we will use to create session objects
Session = sessionmaker(bind=engine)

# instantiate a session object
session = Session()
session.add(jimi) # instance is now pending (not written yet)

# the query initiated the write (flush) to the transaction before the query itself 
our_user = session.query(User).filter_by(name='jimi').first()
print our_user

# check they are the same
print jimi is our_user

# add some more user objects to the session
session.add_all([
     User('wendy', 'Wendy Williams', 'foobar'),
     User('mary', 'Mary Contrary', 'xxg527'),
     User('fred', 'Fred Flinstone', 'blah')])
print session.new 

# modify existing (results in dirty state)
jimi.password = '4f97f479h3'
print session.dirty

# commit all changes
session.commit()

# query SELECT * and show
allUsers = session.query(User).all()
print allUsers

# add a second table with a foreign key constraint
# using the declarative form
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(150), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    # many-to-one bidrectional relations (from Address -> User)
    # from User -> Address it is one-to-many of course
    # this could also be defined in the User class
    user = relationship(User, backref=backref('addresses', order_by=id))

    def __init__(self, email_address):
        self.email_address = email_address

    def __repr__(self):
        return "<Address('%s')>" % self.email_address

metadata.create_all(engine)
