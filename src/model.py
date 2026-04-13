import sqlite3

conn = sqlite3.connect('sqlite.db')

cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))

conn.commit()
conn.close()