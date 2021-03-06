from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()


class World(Base):

    __tablename__ = 'World'

    id = Column(Integer, primary_key=True)

    carriers = Column(Integer)
    humans = Column(Integer)
    time_to_year = Column(String)
    year = Column(Integer)
    dead = Column(Integer)
    recovered = Column(Integer)
    counters = Column(Integer)
    state = Column(String)

    def __repr__(self):
        return '<World(humans="{}", carriers="{}", dead="{}", recovered="{}", state="{}">'.format(self.humans,
            self.carriers,
            self.dead,
            self.recovered,
            self.state)
