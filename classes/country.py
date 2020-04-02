from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Bool

Base = declarative_base()


class Country(Base):

    __tablename__ = 'Countres'

    id = Column(Integer, primary_key=True)

    carriers = Column(Integer)
    name = Column(String)
    humans = Column(Integer)
    condition = Column(Integer)
    medicine = Column(Integer)
    citis = Column(Integer)
    dead = Column(Integer)
    recovered = Column(Integer)

    def __repr__(self):
        return '<Country(name="{}", humans="{}", carriers="{}", dead="{}", recovered="{}">'.format(self.name,
            self.humans,
            self.carriers,
            self.dead,
            self.recovered)
