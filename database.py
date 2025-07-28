import os
import sqlite3

DB_name = "user.db"

# add user
def main():
    while True:
        username = input("enter username: ")
        password = input("enter password: ")
        add_user(username, password)

        const = input("do you want to add another user?(y/n): ").strip().lower()
        if const != 'y':
            print("exiting...")
            break
        
#create a database conntection
def connect_db():
    return sqlite3.connect(DB_name)

# create a table
def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)
                ''')
        conn.commit()

# add user from CLI
def add_user(username: str, password: str):
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            print(f"user {username} added successfully.")
    except sqlite3.IntegrityError:
        print(f"username {username} already exists.")

if __name__ == "__main__":
    main()