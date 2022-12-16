from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

app=FastAPI()

class BlogBase(BaseModel):
    Title:str
    Body:str
    #'pydantic' kod modeline uygun olmasi icin' : 'kullanimina dikkat

class Blog(BlogBase):
    class Config():
        orm_mode=True

class User(BaseModel):
    Name:str
    Password:str
    class Config():
        orm_mode=True

class ShowUser(BaseModel):
    Name:str
    Password:str
    Blogs:List[Blog]=[]
    #gösterilen kullanici bilgileri ile birlikte bloglarida cagirmak icin kullandigimiz fonskiyon
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    Title:str
    Body:str
    class Config():
        orm_mode = True

class Login(BaseModel):
    Username:str
    Password:str

