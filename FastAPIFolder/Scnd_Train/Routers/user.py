from fastapi import APIRouter,Depends
from ..schemas import UserSchema,UserDisplay
from sqlalchemy.orm import Session
from ..database import get_db
from ..db_user import create_user,show_users,show_user,destroy_user,update_user
from typing import List

router = APIRouter(
    tags=["User"],
    prefix="/user",
)


@router.get("/", response_model=List[UserDisplay])
def get_users(db: Session = Depends(get_db)):
    return show_users(db)
    # tum kullanicilari cekmek istedigimiz icin birden fazla 'UserDisplay' response edilecek
    # bu yuzden liste halinde dondurmeye ihtiyacimiz var


@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return show_user(id, db)


@router.post("/new", response_model=UserDisplay)
def new_user(request: UserSchema, db: Session = Depends(get_db)):
    return create_user(db, request)


@router.delete("/delete")
def delete_user(id: int, db: Session = Depends(get_db)):
    return destroy_user(db, id)






