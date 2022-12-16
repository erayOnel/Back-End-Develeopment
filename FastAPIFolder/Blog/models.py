from sqlalchemy import Column,Integer,String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__="Blog_Table"
    Id = Column(Integer,primary_key=True,index=True)
    Title = Column(String)
    Body = Column(String)
    User_id = Column(Integer,ForeignKey("User_Table.Id"))

    creator_of_blog = relationship("User",back_populates="created_blogs_by")
    #'relationship' parametreleri ; 'class_name' ,'table_name'
    # modeller TABLO OLUSTURMAK ICIN kullanilan referanslar,features,parametreler icin bulunur

class User(Base):
    __tablename__="User_Table"
    Id = Column(Integer,primary_key=True,index=True)
    Name = Column(String)
    Password = Column(String)

    created_blogs_by = relationship("Blog",back_populates="creator_of_blog")
    #modeller TABLO OLUSTURMAK ICIN kullanilan referanslar,features,parametreler icin bulunur

