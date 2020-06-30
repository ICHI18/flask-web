import sqlite3

DROP_AUTHORS = "DROP TABLE IF EXISTS authors"

CREATE_AUTHORS = '''CREATE TABLE authors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, bio TEXT)'''
INSERT_AUTHOR  = '''INSERT INTO authors (name,bio) VALUES('ニュートン','「なぜリンゴが木から落ちるのかという疑問から万有引力の法則を発見した」という伝説がある')'''

SELECT_AUTHORS = "SELECT * FROM authors"

conn = sqlite3.connect('bookdb.sqlite3')

c = conn.cursor()
c.execute(DROP_AUTHORS)
c.execute(CREATE_AUTHORS)
c.execute(INSERT_AUTHOR)
conn.commit()

c.execute(SELECT_AUTHORS)
result = c.fetchone()
print(result)