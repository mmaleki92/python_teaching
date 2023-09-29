from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class TableA(Base):
    __tablename__ = 'table_a'
    
    id = Column(Integer, primary_key=True)
    valueA = Column(String)
    b_relationship = relationship("TableB", back_populates="a_relationship")

class TableB(Base):
    # a required attribute for declarative models in SQLAlchemy, indicating the name of the database table the class should map to
    __tablename__ = 'table_b' 
    
    id = Column(Integer, primary_key=True)
    valueB = Column(String)
    a_id = Column(Integer, ForeignKey('table_a.id'))
    a_relationship = relationship("TableA", back_populates="b_relationship")

# Set up the database and session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Insert sample data
a1 = TableA(valueA='A1')
a2 = TableA(valueA='A2')
a3 = TableA(valueA='A3')

b1 = TableB(valueB='B1', a_relationship=a1)
b2 = TableB(valueB='B3', a_relationship=a3)
b3 = TableB(valueB='B4')

session.add_all([a1, a2, a3, b1, b2, b3])
session.commit()

# Query using joins
for a, b in session.query(TableA, TableB).join(TableB, TableA.id == TableB.a_id).all():
    print(a.valueA, b.valueB)
