import sqlite3
import codecs
codecs.register_error("strict", codecs.ignore_errors)
from flask_restful import Resource, reqparse

class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        # 'Büyük' harflerle belirtilen veriler birer fonskiyon
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        # ilk sat?rda bulunan de?eri almak için 'fetchone' komutunu kulland?k
        if row:
            user = cls(*row)
        else:
            user = None
        #cls(class) modülü @classmethod ile birlikte kullan?l?r
        connection.close()
        return user

    @classmethod
    def find_by_id(cls,id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        # 'Büyük' harflerle belirtilen veriler birer fonskiyon
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        # ilk sat?rda bulunan de?eri almak için 'fetchone' komutunu kulland?k
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Insert a username"
                    )

    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Insert a password"
                    )

    def post(self):
        data=UserRegister.parser.parse_args()
        if User.find_by_username(data["username"]):
            return {"message":"A user with that name already exists"},400

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query="INSERT INTO users (username,password)VALUES (?,?)"
        cursor.execute(query,(data["username"],data["password"]))

        connection.commit()
        connection.close()

        return {"massage":"User created successfully"},201



