import sqlite3

conn = sqlite3.connect('eg.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS course (
                id INTEGER PRIMARY KEY, 
                courseName TEXT NOT NULL, 
                instructor TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY, 
                course_id INTEGER, 
                name TEXT NOT NULL,
                grade TEXT NOT NULL, 
                FOREIGN KEY(course_id) REFERENCES course (id))''')

cursor.execute('''INSERT INTO course VALUES (11, 'Science', 'Sweety')''')
cursor.execute('''INSERT INTO course VALUES (12, 'Math', 'Jatin')''')

rows = cursor.fetchall()
for i in rows:
    print(i)

cursor.execute('''INSERT INTO students VALUES (1, 11, 'Sasha', 'B')''')
cursor.execute('''INSERT INTO students VALUES (2, 11, 'Talika', 'C')''')
cursor.execute('''INSERT INTO students VALUES (3, 12, 'Farha', 'A')''')
cursor.execute('''INSERT INTO students VALUES (4, 11, 'Jyoti', 'B')''')
cursor.execute('''INSERT INTO students VALUES (5, 12, 'Vani', 'C')''')

(cursor.execute('SELECT * FROM students'))
rows = cursor.fetchall()
for i in rows:
    print(i)

print()

# QUERY database
cursor.execute('''SELECT * FROM students ''')
rows = cursor.fetchall()

for row in rows:
    print(row)
print()

# Query and print all data from 'course'
cursor.execute('SELECT * FROM course')
r = cursor.fetchall()
for row in r:
    print(row)

print()  # Print a blank line for separation

# Combine data from 'students' and 'course' using LEFT JOIN
cursor.execute('''SELECT students.id, students.name, students.grade, course.courseName, course.instructor
                  FROM students
                  LEFT JOIN course ON students.course_id = course.id''')
combined_rows = cursor.fetchall()
for row in combined_rows:
    print(row)

# Commit changes and close connection
conn.commit()
conn.close()