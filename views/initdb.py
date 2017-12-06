from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base

engine = create_engine('postgresql://jitniran:sqlsecret@localhost/sports')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
