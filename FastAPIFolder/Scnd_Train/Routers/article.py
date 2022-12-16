from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import ArticleBase, ArticleDisplay
from ..db_article import create_article, get_article
from ..oauth2 import oauth2_scheme

router = APIRouter(
    prefix="/article",
    tags=["Articles"]
)


@router.get("/", response_model=ArticleDisplay)
def show_article(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return get_article(db, id)


@router.post("/create", response_model=ArticleDisplay)
def new_article(request: ArticleBase, db: Session = Depends(get_db)):
    return create_article(db, request)




















































