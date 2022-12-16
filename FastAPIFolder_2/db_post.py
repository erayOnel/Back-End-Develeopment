import datetime
from sqlalchemy.orm import Session
from .models import PostModel
from .schemas import PostSchema
from fastapi import status, HTTPException


def create_new_post(db: Session, request: PostSchema):
    new_post = PostModel(
        Title=request.Title,
        Content=request.Content,
        Author=request.Author,
        Timestamp=datetime.datetime.now(),
        Image_Url=request.Image_Url,
        # 'request' parametresi bilginin iletilecegi noktayi gosterir
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_posts(db: Session):
    all_posts = db.query(PostModel).all()
    if not all_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Flat")
    return all_posts


def get_post(id: int, db: Session):
    get_spec = db.query(PostModel).filter(PostModel.ID == id).first()
    if not get_spec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"This post with {id} id not exists")
    else:
        return get_spec


def delete_post(id: int, db: Session):
    will_deleted = db.query(PostModel).filter(PostModel.ID == id).first()
    if not will_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"This post with {id} id not exists")
    else:
        db.delete(will_deleted)
        db.commit()
        return {
            "Deleted item": will_deleted
        }


