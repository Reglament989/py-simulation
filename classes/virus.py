from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Bool

Base = declarative_base()


class Virus(Base):

    __tablename__ = 'Virus'

    id = Column(Integer, primary_key=True)
    gen = Column(String)
    gear = Column(String)
    disease = Column(String)
    moralyti = Column(String)
    mutation = Column(String)
    kills = Column(Integer)
    recovered = Column(Integer)
        
    def __repr__(self):
        return '<Virus(gen="{}", moralyti="{}">'.format(self.gen, self.moralyti)
