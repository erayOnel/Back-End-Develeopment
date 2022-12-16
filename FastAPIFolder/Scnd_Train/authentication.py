from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .database import get_db
from . import models
from .hashing import Hash
from . import oauth2


router=APIRouter(
    tags=["Authentication"]
)

@router.post("/token")
#burada belirtilen token 'oauth2' icinde belirtilen 'tokenUrl'den cagirilmaktadir(tokenUrl degiskeni dogru atanmali)
def get_token(request:OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user = db.query(models.db_User).filter(models.db_User.Username == request.username).first()
    #fonksiyon icinde belirtilen 'user' degeri fonksiyonun geri kalaninda da 'user' olarak hitabiyla kullanilmali
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="This username is not exists")
    if not Hash.verify(user.Password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect password")

    access_token = oauth2.create_access_token(data={'sub':user.Username})

    return{
        "Access_Token":access_token,
        "Token_Type":"bearer",
        "User_Id":user.Id,
        "Username":user.Username,
    }

# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VybmFtZV8xIiwiZXhwIjoxNjYxOTUyOTczfQ.Q9nw9HRp9kL2jZWAUDX8LJW1pqltRY5gqwBjg-VM-5g

