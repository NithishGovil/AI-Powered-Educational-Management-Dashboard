import sqlite3

conn = sqlite3.connect("college.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    year INTEGER,
    attendance REAL,
    marks REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS fees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    amount REAL,
    status TEXT
)
""")

conn.commit()

conn.close()

print("Database Created Successfully")