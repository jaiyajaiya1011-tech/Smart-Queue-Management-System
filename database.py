import sqlite3

def create_database():
    conn = sqlite3.connect("queue.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token_number TEXT NOT NULL,
            service TEXT NOT NULL,
            status TEXT DEFAULT 'Waiting'
        )
    """)

    conn.commit()
    conn.close()

create_database()