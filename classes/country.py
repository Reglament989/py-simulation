from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

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
        return '''
<Country(name="{}",
    humans="{}",
    condition="{}",
    medicine="{}",
    citis="{}",
    carriers="{}",
    dead="{}",
    recovered="{}">'''.format(self.name,
            self.humans,
            self.condition,
            self.medicine,
            self.citis,
            self.carriers,
            self.dead,
            self.recovered)


    name_countres = [
        'Russia',
        'USA',
        'Poland',
        'Germany',
        'China',
        'UAE',
        'Japan',
        'Corea',
        'Australia',
        'Netherlands',
    ]
