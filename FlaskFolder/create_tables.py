import sqlite3
import codecs
codecs.register_error("strict", codecs.ignore_errors)

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

#create_table="CREATE TABLE IF NOT EXISTS items(name text,price real)"
#cursor.execute(create_table)
#cursor.execute("INSERT INTO items VALUES('test',10.85)")

connection.commit()

connection.close()












































