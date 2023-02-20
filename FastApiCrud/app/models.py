from sqlalchemy import  Column, Integer, String
from .config import Base, engine

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username =  Column(String(50))
    password = Column(String(50))

Base.metadata.create_all(engine)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    content =  Column(String(50))
    

Base.metadata.create_all(engine)