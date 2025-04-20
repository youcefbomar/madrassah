from database import *


def payment_id_changer(payments_list) :
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    for row_number, row in enumerate(payments_list) :
        enrollment_id = row[1]
        
        cursor.execute("SELECT * FROM enrollment WHERE id = ?", (enrollment_id,))
        enrollment = cursor.fetchone()

        student_id = enrollment[1]
        classe_id = enrollment[2]

        cursor.execute("SELECT * FROM classes WHERE id = ?", (classe_id,))
        classe = cursor.fetchone()

        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()

        cursor.execute("SELECT * FROM teachers WHERE id = ?", (classe[1],))
        teacher = cursor.fetchone()

        student_name , teacher_name = student[1] , teacher[1]

        payments_list[row_number][1] = student_name
        payments_list[row_number].insert(2,teacher_name)


    return payments_list
        




def creating_all_tables() :

    creates_students_table()
    creates_teachers_table()
    creates_classes_table()
    creates_payments_table()
    creates_enrollment_table()


def enrollment_extractor():

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("SELECT * FROM ENROLLMENT")



def returning_students_table():

    rows = []

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("SELECT * FROM students")
    users = cursor.fetchall()  # Get all rows
    for user in users:
        rows.append(user)
    
    return rows



def returning_teachers_table():

    rows = []

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("SELECT * FROM teachers")
    users = cursor.fetchall()  # Get all rows
    for user in users:
        rows.append(user)
    
    return rows



def returning_payments_table():

    rows = []

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("SELECT * FROM payments")
    users = [list(row) for row in cursor.fetchall()]

    for user in users:

        rows.append(user)

    rows = payment_id_changer(rows)

    return rows


def returning_classes_table():

    rows = []

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("SELECT * FROM classes")
    users = cursor.fetchall()  # Get all rows
    for user in users:
        rows.append(user)
    
    return rows




if __name__ == "__main__" :
    
    
    print(returning_classes_table()[1])

