import sqlite3
from sqlite3 import Error

database = r"database.sqlite"

conn = sqlite3.connect(database)
cur = conn.cursor()


cur.execute(f"""

DROP TABLE user

""")

cur.execute(f"""
        
    CREATE TABLE user (
        u_userid integer(100),
        u_fullname varchar(100),
        u_email varchar(100),
        u_phonenumber integer(100),
        u_username varchar(100),
        u_password varchar(100),
        u_type varchar(100)
    )""")

