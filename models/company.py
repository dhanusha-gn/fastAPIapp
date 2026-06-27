from sqlalchemy import Column,Integer,String,Enum,relationship
from database import  Base,engine,SessionLocal

class Company(base):
    __tablename__="companies" 
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String,nulllabel=False,index=True)
    email=Column(String,unique=True)
    phone=Column(String,unique=True)
    jobs=relationship("Job",back_populates="company")
    