from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv('MYSQL_USER')
db_password = os.getenv('MYSQL_PASSWORD')
db_name = os.getenv('MYSQL_DATABASE')

engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@localhost/{db_name}", echo=True)
if not engine:
    exit("Error: no token provided")
else:
    print('DB connected!')

Base = declarative_base()


class Vehicle(Base):
    __tablename__ = 'Vehicle'

    id = Column(Integer, primary_key=True)
    brand = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    fuel = Column(String(250), nullable=False)
    engine = Column(String(250), nullable=False)
    year = Column(Integer, nullable=False)
    vin = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"))
    token = Column(String(250), nullable=False)
    User = relationship("Users")


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    phone = Column(String(250), nullable=False)
    vehicle = relationship("Vehicle")


Base.metadata.create_all(engine)
