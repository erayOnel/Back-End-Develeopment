from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from ..schemas import ShowUser,ShowBlog,User,Blog
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog

router=APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

@router.get("/",response_model=List[ShowBlog],status_code=status.HTTP_200_OK)
#'response_model' verinin gorsellestirilme seklini ayarlamaya yarar
def all(db:Session=Depends(get_db)):
    return blog.get_all(db)

@router.post("/",status_code=status.HTTP_202_ACCEPTED)
def create(request:Blog,db:Session=Depends(get_db)):
    return blog.create_blog(request,db)

@router.delete("/{id}",status_code=status.HTTP_202_ACCEPTED)
def delete(id:int,db:Session=Depends(get_db)):
    return blog.destroy_blog(id,db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:Blog,db:Session=Depends(get_db)):
    return blog.update(id,request,db)

@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_specific(id:int,db:Session=Depends(get_db)):
    return blog.get_one_blog(id,db)




