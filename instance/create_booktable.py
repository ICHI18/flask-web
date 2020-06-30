import sqlite3

DROP_BOOKS = "DROP TABLE IF EXISTS books"
CREATE_BOOKS = '''CREATE TABLE books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    cover TEXT DEFAULT 'book.png' )'''

conn = sqlite3.connect('bookdb.sqlite3')
c = conn.cursor()
c.execute(DROP_BOOKS)
c.execute(CREATE_BOOKS)
conn.commit()
conn.close()
