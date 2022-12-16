import sqlite3
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
import codecs
#from item import Item
codecs.register_error("strict", codecs.ignore_errors)
from user import UserRegister


app=Flask(__name__)
app.secret_key="Cat"
api=Api(app)

jwt=JWT(app,authenticate,identity)  #JWT modülü otomatik olarak /auth yolunu oluşturuyor

items=[]

class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                             )
    @jwt_required()
    def get(self,name):
        connection=sqlite3.connect("data.db")
        cursor =connection.cursor()
        query="SELECT * FROM items WHERE name=?"
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        connection.close()

        if row:
            return {"item":{"name":row[0],"price":row[1]}}
        return{"message":"item not found"},404
    #     item=next(filter(lambda x:x["name"]==name,items ),None)
    #     return {"item":item},200 if item else 404
    def post(self, name):
        if (next(filter(lambda x:x["name"]==name,items),None)):
            return {"message":"an item with '{}' already exists".format(name)},400

        data = Item.parser.parse_args()
        #'create' fonksiyonu için 'POST' metodu tercih edilebilir
        # force="True" parametresi 'postman' da tanımladığımız content type değerinin görevini görür(postmanda tanıımlamaya gerek kalmaz)
        # silent="True" parametresi hata mesajı yerine 'None' değeri verir
        item={"name":name,"price":data["price"]}
        items.append(item)
        return item,201


    def put(self,name):
#'update' fonskiyonu için 'PUT' metodu tercih edilebilir
            data=Item.parser.parse_args()
            item=next(filter(lambda x: x["name"]==name,items),None)
            if item is None:
                item = {"name": name, "price": data["price"]}
                items.append(item)
            else:
                item.update(data)
            return item

    def delete(self, name):
         global items
         items=list(filter(lambda x:x["name"] != name,items))
         return {"message":"Item just deleted"}

class ItemList(Resource):
    def get(self):
        return {"items":items}

api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(UserRegister,"/register")

if __name__ == "__main__":
    import test
    from waitress import serve
    serve(app, host="127.0.0.1",port=3554)


