from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes="bcrypt",deprecated="auto")

class Hash:
    def bcrypt(password:str):
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(hashed_password,plain_password):
        return (plain_password,hashed_password)




