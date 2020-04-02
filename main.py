from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('sqlite:///simulation.db', echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()


class BasicSimulation():
    def __init__(self):
        pass
        
        

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
    feth_data()
