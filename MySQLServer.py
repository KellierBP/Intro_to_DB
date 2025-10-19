#!/usr/bin/env python3
"""
MySQLServer.py
A simple Python script to create a MySQL database named 'alx_book_store'.
"""

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update credentials as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # <-- Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
