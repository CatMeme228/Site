import sqlite3
connection= sqlite3.connect('database.db')
cursor= connection.cursor()

with open('schema.sql') as f:
   tmp= f.read()
cursor.executescript(tmp)