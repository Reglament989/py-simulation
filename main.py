from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from pprint import pprint
from classes import (
    world,
    humanoid,
    country
)
import random


engine = create_engine('sqlite:///simulation.db', echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()


states = ['worried', 'panic', 'fear', 'relaxed', 'normal']

class BasicSimulation():

    need_days = 0
    day = 0
    countres = {}
    WORLD = None 
    VIRUS = None


    def __init__(self, days):

        self.__class__.need_days = days

        self.__class__.WORLD = world.World(carriers=0,
            humans=0,
            time_to_year='Winter',
            year=2020,
            dead=0,
            counters=0,
            recovered=0,
            state=states[-1])

        self.__class__.VIRUS = virus.Virus(name=random.choice(virus.Virus.names_virus),
            gen=random.choice(virus.Virus.virus_gens),
            gear=random.choice(virus.Virus.gears),
            moralyti=random.randrange(10,50),
            spreading_power=random.randrange(10,30),
            kills=0,
            carriers=0,
            recovered=0)

        for Country_name in country.Country.name_countres:
            self.__class__.countres[Country_name] = {"country": country.Country(carriers=0,
                    name=Country_name,
                    humans=random.randrange(int(10E2),int(10E3)),
                    condition=random.randrange(10,80),
                    medicine=random.randrange(10,80),
                    citis=0,
                    dead=0,
                    recovered=0)
                }
            
            self.__class__.countres[Country_name]['humans'] = [
                humanoid.Human(age=random.randrange(1,78),
                    job=random.choice(humanoid.Human.types_of_work),
                    wealth=random.randrange(3,80),
                    country=Country_name,
                    state=states[-1]) for _ in range(self.__class__.countres[Country_name]['country'].humans)
            ]
        for Country_name in name_countres:
            pprint(self.__class__.countres[Country_name]['country'])
        Base.metadata.create_all(engine)
        session.commit()

    def next_year(self):
        self.__class__.WORLD.year += 1
        session.commit()

    def start(self):
        while self.__class__.day <= self.__class__.need_days:
            if self.__class__.day > 365:
                self.next_year(self)
            else:
                pass

            

            self.__class__.day += 1

        
        

def feth_data():
    query = session.query(Human).filter_by(age=19)
    other = query.first()
    print(other)



def main():
    Base.metadata.create_all(engine)
    human = Human(age=19, state='OK')
    session.add(human)
    session.commit()
    



if __name__ == '__main__':
    # main()
    BasicSimulation()
