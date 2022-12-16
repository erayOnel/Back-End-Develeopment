from pydantic import BaseModel
from typing import List
from typing import Optional

class Article(BaseModel):
    Title:str
    Content:str
    Published:bool
    class Config():
        orm_mode = True
        #burda bulunan article 'UserDisplay' ile donucek olan items(blogs) listesi icin var

class UserSchema(BaseModel):
    Username:str
    Password:str
    Email:str

class UserDisplay(BaseModel):
    Username:str
    Password:str
    Items:List[Article]=[]
    class Config():
        orm_mode = True
        #bir 'database'i bir digerine adapte etmek icin ihtiyacimiz olan sinif

class User(BaseModel):
    Id:int
    Username:str
    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    Title:str
    Content:str
    Published:bool
    Creator_Id:int
    #'ArticleBase' request,
class ArticleDisplay(BaseModel):
    Title:str
    Content:str
    Published:bool
    User:User
    #'User' icinde tanimlanan classdan id ve username cagiriyor
    #olusturulan article bir 'id'ye sahip olmali
    class Config():
        orm_mode = True
    #'ArticleDisplay' ise response icin var

class ProductSchema(BaseModel):
    Title: str
    Description: str
    Price: float






