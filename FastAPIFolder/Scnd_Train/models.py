from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy import Column,String,Integer,Boolean,ForeignKey


class db_User(Base):
    __tablename__="User_Table"
    Id = Column(Integer,primary_key=True,index=True)
    Username = Column(String)
    Password = Column(String)
    Email = Column(String)
    Items = relationship("db_Article",back_populates="User")

class db_Article(Base):
    __tablename__="Articles"
    Id=Column(Integer,primary_key=True, index=True)
    Title = Column(String)
    Content=Column(String)
    Published=Column(Boolean)
    Creator_Id=Column(Integer,ForeignKey("User_Table.Id"))
    User=relationship("db_User",back_populates="Items")








