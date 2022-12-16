from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from ..token import create_access_token

router=APIRouter(
    tags=["Authentication"]
)

@router.post("/login")
def login(request:schemas.Login,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.Name == request.Username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid credentials")
    if not Hash.verify(user.password,request.Password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect password")

    access_token=create_access_token(data={"sub":user.Name})
    return {"access_token":access_token,"token_type":"bearer"}




