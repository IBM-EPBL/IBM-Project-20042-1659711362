import sqlite3 as sql
con=sql.connect("database.db")
cur=con.cursor()
cur.execute("drop table if exists users")
cur.execute("CREATE TABLE users (id	INTEGER,username TEXT NOT NULL,email TEXT NOT NULL,password	TEXT NOT NULL,date_posted	DATE NOT NULL,PRIMARY KEY(id));")
cur.close()