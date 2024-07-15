import sqlite3
import hashlib
#connect to the SQLite database name 'user.db'
#if the database does not exist it wil be created
conn = sqlite3.connect("user.db")
cur = conn.cursor() #this creates a cursor object to interact with a databse
cur.execute( """
CREATE TABLE IF NOT EXISTS userdata(
    id INTERGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""
)
#Define four sets of usernames and passwords
#Hash the passwords using Sha-256 for security purposes
username1, password1 = "1", hashlib.sha256("password1".encode()).hexdigest()
username2, password2 = "2", hashlib.sha256("password2".encode()).hexdigest()
username3, password3 = "3", hashlib.sha256("password3".encode()).hexdigest()
username4, password4 = "4", hashlib.sha256("password4".encode()).hexdigest()
#Insert these usernames and hashed passwords into the 'userdata' table
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?,?)", (username4, password4))
#commit changes
conn.commit()







