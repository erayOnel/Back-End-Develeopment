#modelleri tasarlanmis database
#(engine-database-sessionmaker)olustur
#'parametre ve ornek alinan' semalari(schemas) olustur
#'repository' fonksiyonlarini olustur(blog-user-auth)
#'repository'leri cagirabilecek 'router' noktalarini olustur('router'i 'app'e dahil etmeyi unutma)
#gerekiyorsa sifreleri 'hash'lemeyi unutma(repository)

from fastapi import FastAPI
from .database import engine
from . import models
from .Routers import blog,user,login

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)

