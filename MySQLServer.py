import mysql.connector

try:
    # CONNECT TO MYSQL SERVER
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cellobiose1234"
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # CREATE DATABASE IF NOT EXISTS
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
    print("Error while connecting to MySQL")

finally:
    # CLOSE CONNECTION
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
