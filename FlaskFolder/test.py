import sqlite3
import codecs
codecs.register_error("strict", codecs.ignore_errors)
connection=sqlite3.connect("data.db")
cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EXISTS users(id int,username text,password text)"
cursor.execute(create_table)

user=(1,"Rolf","qwer")
insert_query="INSERT INTO users VALUES (?,?,?)"
#içine değerleri yazmak istediğimiz şablon 'users' ve değerler ise 'VALUES' komutu ile belirtilir
cursor.execute(insert_query,user)

users=[
    (2,"Bob","zxc"),
    (3,"Violet","qwe"),
    (4,"Carl","asd")
]
insert_query="INSERT INTO users VALUES (?,?,?)"
cursor.executemany(insert_query,users)

select_query="SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)
connection.commit()
#yapılan değişiklikleri connect ettiğimiz(data.db) database içinde kayıt etmek için kullan?l?r
connection.close()





































