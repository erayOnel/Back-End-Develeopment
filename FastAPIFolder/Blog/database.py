from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#engine create
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL="sqlite:///./for_blog.db"
#database route
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
#tablo olusturmak icin kullanilabilir fonksiyon
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    #'database'e hitap icin kullanabilecegimiz atamayı yaptıgımız yer
    try:
        yield db
    finally:
        db.close()
