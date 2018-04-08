import sqlite3

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

def FirstDb():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
    cursor.close()
    conn.commit()
    conn.close()

