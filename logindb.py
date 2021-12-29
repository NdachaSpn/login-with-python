# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:06:43 2021

@author: Simon
"""
#create db and establish connection
from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user="root",
        password=getpass("Enter password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE login"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)

except Error as e:
    print(e)


#creating table in db

create_usertable_table_query = """
CREATE TABLE usertable(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    
)
"""
with connection.cursor() as cursor:
    cursor.execute(create_usertable_table_query)
    connection.commit()
