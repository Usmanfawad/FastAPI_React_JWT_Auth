from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///fastapi.db")
Base = declarative_base()


print("Created all!")

app = FastAPI()