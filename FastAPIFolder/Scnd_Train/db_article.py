from sqlalchemy.orm import Session
from .models import db_Article
from .schemas import ArticleBase
from fastapi import HTTPException,status
from .teapot import StoryException


def create_article(db:Session,request:ArticleBase):
    if request.Content.startswith("Once upon a time"):
        raise StoryException("I'm a teapot")
    new_article = db_Article(
        Title=request.Title,
        Content=request.Content,
        Published=request.Published,
        Creator_Id=request.Creator_Id,
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db:Session,id:int):
    article = db.query(db_Article).filter(db_Article.Id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"This article with {id} id not exists")
    return article





