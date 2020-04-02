from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()

class Human(Base):

    __tablename__ = 'humans'

    id = Column(Integer, primary_key=True)

    age = Column(Integer)
    family = Column(String)
    job = Column(String)
    wealth = Column(String)
    country = Column(String)
    sity = Column(String)
    state = Column(String)

    def __repr__(self):
        return '<Human(age="{}", state="{}">'.format(self.age, self.state)
