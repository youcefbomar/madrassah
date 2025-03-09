import sqlite3



def creates_students_table ():

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
    """)

    conn.commit()
    cursor.close()


def creates_teachers_table() :

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
    """)

    conn.commit()
    cursor.close()



def add_student(name, birth_year, phone_number):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students (name, birth_year, phone_number) VALUES (?, ?, ?)", (name, birth_year, phone_number))


    conn.commit()
    cursor.close()


def add_teacher(name, birth_year, phone_number):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO teachers (name, birth_year, phone_number) VALUES (?, ?, ?)", (name, birth_year, phone_number))


    conn.commit()
    cursor.close()


'''
creates_students_table()
creates_teachers_table()
add_teacher('Joseph', '2005', '066988557')
add_student('Joseph', '2005', '066988557')

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
users = cursor.fetchall()  # Get all rows
for user in users:
    print(user)  # Example output: (1, 'Alice', 25)


cursor.execute("SELECT * FROM teachers")
users = cursor.fetchall()  # Get all rows
for user in users:
    print(user)  # Example output: (1, 'Alice', 25)

conn.commit()
cursor.close()
'''
