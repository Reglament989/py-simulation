from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Bool

Base = declarative_base()


class Virus(Base):

    __tablename__ = 'Virus'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gen = Column(String)
    gear = Column(String)
    # disease = Column(String)
    moralyti = Column(Integer)
    # mutation = Column(Integer)
    kills = Column(Integer)
    spreading_power = Column(Integer)
    carriers = Column(Integer)
    recovered = Column(Integer)
        
    def __repr__(self):
        return '<Virus(name="{}", gen="{}", moralyti="{}", kills="{}", carriers="{}", spreading_power="{}">'.format(self.name,
            self.gen,
            self.moralyti,
            self.kills,
            self,carriers,
            self.spreading_power)

    names_virus = [
        'COVid-19',
        'Pih pau',
        'Ebola',
        'Sibirka',
        'Fear_Death',
    ]

    virus_gens = ['.']

    gears = [
        'air',
        'water',
        'blood',
        # 'animals',
    ]
