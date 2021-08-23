import sqlite3 as sl
import os

# THIS FUNCTION CAN BE CALLED DURING INITIAL CONFIG
def create():
    
    os.remove("test_db")
    con=sl.connect('test_db')

    with con:
        con.execute("""
            CREATE TABLE USER (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                gender TEXT,
                weight INTEGER,
                Height INTEGER,
                Activity TEXT,
                Goal TEXT
            );
        """)
    insert()

# THIS FUNCTION CAN BE CALLED TO UPDATE DATA
def insert(height, weight):
    con=sl.connect('test_db')
    
    '''
    
    USER INPUT CAN BE TAKEN HERE
    
    '''
    
    with con:
        sql = 'INSERT OR REPLACE INTO USER (id, name, age, weight, Height) values(?, ?, ?, ?, ?)'
    data = [
        (1 , 'Alice', 21, weight, height)
    ]
    
    with con:
        con.executemany(sql, data)
        
    with con:
       data = con.execute("SELECT * FROM USER WHERE age <= 24")
       for row in data:
           print(row)
 
insert(160, 60)