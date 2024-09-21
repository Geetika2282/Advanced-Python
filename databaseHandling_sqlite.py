import sqlite3
conn = sqlite3.connect('demo1.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, 
address TEXT NOT NULL, mobile INTEGER, email TEXT NOT NULL)''')

cursor.execute('''INSERT INTO data VALUES(11, 'Alice', 'Wadi', '1234', 'j@gmail.com')''')
cursor.execute('''INSERT INTO data VALUES(12, 'Bob', 'Bhor', '4657', 'j@gmail.com')''')
cursor.execute('''INSERT INTO data VALUES(13, 'Champa', 'Dhanori', '178234', 'j@gmail.com')''')
cursor.execute('''INSERT INTO data VALUES(14, 'Dhanno', 'Jodhpur', '786543', 'j@gmail.com')''')

conn.commit()
cursor.execute('SELECT * FROM data')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()


