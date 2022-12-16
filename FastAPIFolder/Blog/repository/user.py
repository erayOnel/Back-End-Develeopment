from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..hashing import Hash,pwd_cxt
from ..models import User
from ..database import get_db

def create_user(request,db:Session=Depends(get_db)):
    hashed_password=pwd_cxt.hash(request.Password)
    new_user=User(Name=request.Name,Password=request.Password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show_user(id,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.Id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"A user with {id} id is not exists")
    # if not Hash.verify(user.Password,requests.Password):
    return user


