import sqlite3

conn = sqlite3.connect('pdt.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS pdt (
id INTEGER PRIMARY KEY, 
name TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS cust (
id INTEGER PRIMARY KEY, 
pdt_id INTEGER, 
name TEXT NOT NULL, 
FOREIGN KEY(pdt_id) REFERENCES pdt(id) 
)''')

cursor.execute("INSERT INTO pdt VALUES (11, 'book')")
cursor.execute("INSERT INTO pdt VALUES (12, 'coffee')")
cursor.execute("SELECT * FROM pdt")
pd = cursor.fetchall()

cursor.execute("INSERT INTO cust VALUES (1, 11, 'Rob')")
cursor.execute("INSERT INTO cust VALUES (2, 12, 'Rex')")
cursor.execute("SELECT * FROM cust")
cus = cursor.fetchall()

print("Product: ")
for i in pd:
    print(i)

print("Customer: ")
for i in cus:
    print(i)

print("Join: ")
cursor.execute('''SELECT cust.id, cust.name,  pdt.name
                  FROM cust
                  LEFT JOIN pdt ON cust.pdt_id = pdt.id''')
combined_rows = cursor.fetchall()
for row in combined_rows:
    print(row)


cursor.close()
conn.close()
