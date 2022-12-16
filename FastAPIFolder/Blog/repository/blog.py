from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas


def get_all(db:Session):
    all_blog=db.query(models.Blog).all()
    return all_blog
    #'return' komutu ekrana dondurulen(cikti,gorsellestirilen)veriyi belirtir

def create_blog(request,db:Session):
    #request 'database' ile iletisim(veri sorgusu) icin gereklidir
    new_blog=models.Blog(Title = request.Title,Body = request.Body,User_id = 1)
    #new_blog=db.query(Title = models.Blog.Title,Body = models.Blog.Body,user_id = 1)
    #'query' fonksiyonu sorgu ici kullanilir ('get')
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy_blog(id,db:Session):
    delete_blog=db.query(models.Blog).filter(models.Blog.Id == id).first()
    # delete_blog=(db.query(models.Blog.Id)==id)
    if not delete_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"A blog with {id} id not exists")
    delete_blog.delete(synchronize_session=False)
    db.commit()

def update(id,request:schemas.Blog,db:Session):
    #update yapilmak istenen 'feature'lari request parametresi ile belirttik
    put_update=db.query(models.Blog).filter(models.Blog.Id == id)
    if not put_update.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"A blog with {id} id not exists")
    put_update.update(request.dict())
    db.commit()
    db.refresh(put_update)
    return put_update

def get_one_blog(id,db:Session):
    show_specific=db.query(models.Blog).filter(models.Blog.Id == id)
    if not show_specific:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"A blog with {id} id doesn't found ")
    return show_specific




