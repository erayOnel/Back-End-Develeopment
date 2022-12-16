from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from base64 import b64encode
from os import urandom


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

random_bytes = urandom(64)
token = b64encode(random_bytes).decode()

SECRET_KEY = f'{token}'
#'SECRET_KEY' random generate edilmis unique bir 'key'dir
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
#boilerplate





