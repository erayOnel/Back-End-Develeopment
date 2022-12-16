from fastapi import APIRouter,status,Depends
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import user

router=APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    #ihtiyacimiz olan referanslari/parametreleri(kullanici adi,sifre)'schemas' üzerinden aliyoruz
    return user.create_user(request,db)

@router.get("/{id}",status_code=status.HTTP_200_OK)
def show_user(id:int,db:Session=Depends(get_db)):
    return user.show_user(id,db)


