from sqlalchemy.orm import Session
from .schemas import UserSchema
from .models import db_User
from .hashing import Hash
from fastapi import Depends,HTTPException,status
from .database import get_db

def create_user(db:Session,request:UserSchema):
    #'request' olarak tanimlanan sema(UserSchema)
    #icindeki degerleri asagidaki modele ait degiskenlere(db_User)atiyoruz
    new_user = db_User(
        Username = request.Username,
        Password = Hash.bcrypt(request.Password),
        Email = request.Email,
    )
    if not new_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="This user is not exists")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    #'new_user' icin otomatik id atamasinin calismasi icin refresh kullaniyoruz

def show_user(id:int,db:Session = Depends(get_db)):
    show_one = db.query(db_User).filter(db_User.Id == id).first()
    if not id == db_User.Id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="This user is not exists")
    return show_one
    #fonksiyon girdisinde bulunan (kullanicinin girdigi) id
    #ile db_User icinde bulunan id (Id)'nin dogrulugnun kontrol ediyoruz('first' unutma)

def show_users(db:Session):
    return db.query(db_User).all()

def update_user(db:Session,id:int,request:UserSchema):
    for_update = db.query(db_User).fiter(db_User.Id == id).first()
    for_update.update({
        db_User.Username:request.Username,
        db_User.Password:request.Password,
        db_User.Email:request.Email
    })
    if not for_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="This user is not exists")
    db.commit()
    db.refresh(for_update)
    return "User's updated"

def destroy_user(db:Session,id:int):
    for_delete=db.query(db_User).filter(db_User.Id == id).first()
    if not for_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="This user is not exists")
    db.delete(for_delete)
    db.commit()
    return "User's deleted"







