import sqlite3
connection= sqlite3.connect('database.db')
connection= sqlite3.connect('users.db')

#with open('schema.sql') as f:
#    connection.executescript(f.read())

with open('schema2.sql') as f:
    connection.executescript(f.read())