from fastapi import APIRouter, Depends, File, UploadFile
from FastAPIFolder_2 import models
from sqlalchemy.orm import Session
from ..database import get_db
from .. import db_post
from .. import schemas
import random
import string
import shutil

router = APIRouter(
    prefix="/post",
    tags=["Post"]
)


@router.post("/")
def create_post(request: schemas.PostSchema, db: Session = Depends(get_db)):
    return db_post.create_new_post(db, request)


@router.get("/get_all")
def get_posts(db: Session = Depends(get_db)):
    return db_post.get_posts(db)


@router.get("/get_spec")
def get_specific(id, db: Session = Depends(get_db)):
    return db_post.get_post(id, db)


@router.delete("/delete")
def destroy(id, db: Session = Depends(get_db)):
    return db_post.delete_post(id, db)


@router.post("/image")
def upload_image(image: UploadFile = File(Ellipsis)):
    letter = string.ascii_letters
    random_string = "".join(random.choice(letter) for x in range(6))
    new = f"_{random_string}."
    file_name = new.join(image.filename.rsplit(".", 1))
    # 'rsplit' icinde belirtilen ikinci parametre en fazla kac farkli listeye ayrilacagini belirleyen parametre
    path = f"C:/Users/erayo/PycharmProjects/pythonProject/FastAPIFolder_2/images/{file_name}"
    # path = f"/images/{file_name}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {"Item saved as": path}

