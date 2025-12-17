# Mysql Connection

import mysql.connector
from password_once import get_decrypted_password

def connect_to_mysql():
    connection=mysql.connector.connect(
        host='localhost',       
        user='root',
        password=get_decrypted_password(),
        database='world'       # Database name
    )

    print("Connected to MySQL Succesfully")
    print(get_decrypted_password())
    connection.close()

if __name__=="__main__":
    connect_to_mysql()