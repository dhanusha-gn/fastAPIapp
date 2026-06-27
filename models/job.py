from sqlalchemy import Column,Integer,String,Enum,ForeignKey,realtionship
from models.company import Company
from database import Base,engine,SessionLocal




class Job(base):
    __tablename__="jobs" 
    id = Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    description=Column(String)
    salary=Column(Integer)
    company=Column,Integer,ForeignKey("companies.id")
    company=realtionship("Company",back_populates="jobs")