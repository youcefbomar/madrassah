from database import *
from PySide6.QtWidgets import QTableWidgetItem


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




def classes_id_changer(classes_list) :
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    for row_number, row in enumerate(classes_list) :
        teacher_id = row[1]

        cursor.execute("SELECT * FROM teachers WHERE id = ?", (teacher_id,))
        teacher_name = cursor.fetchone()[1]

        classes_list[row_number][1] = teacher_name


    return classes_list



def creating_all_tables() :

    creates_students_table()
    creates_teachers_table()
    creates_classes_table()
    creates_payments_table()
    creates_enrollment_table()


def enrollment_extractor():

    creating_all_tables()

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("SELECT * FROM ENROLLMENT")



def returning_students_table():
    rows = []

    try :
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("SELECT * FROM students")
        users = cursor.fetchall()  # Get all rows
        for user in users:
            rows.append(user)

    except :
        pass

    return rows



def returning_teachers_table():
    rows = []

    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("SELECT * FROM teachers")
        users = cursor.fetchall()  # Get all rows
        for user in users:
            rows.append(user)

    except:
        pass

    return rows


def returning_teachers_names():
    rows = []

    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("SELECT * FROM teachers")
        users = cursor.fetchall()  # Get all rows
        for user in users:
            rows.append(user[1])

    except:
        pass

    return rows    



def returning_payments_table():
    rows = []

    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("SELECT * FROM payments")
        users = [list(row) for row in cursor.fetchall()]

        for user in users:

            rows.append(user)

        rows = payment_id_changer(rows)
    except:
        pass

    return rows


def returning_classes_table():
    rows = []

    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        cursor.execute("SELECT * FROM classes")
        users = [list(row) for row in cursor.fetchall()]

        for user in users:

            rows.append(user)

        rows = classes_id_changer(rows)

    except:
        pass
    
    return rows


def get_number_of_teachers() :

    count = "0"
    try :
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Execute the count query
        cursor.execute("SELECT COUNT(*) FROM teachers")
        count = str(cursor.fetchone()[0])
    except :
        pass

    return count


def get_number_of_students() :
    count = "0"
    try :
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Execute the count query
        cursor.execute("SELECT COUNT(*) FROM students")
        count = str(cursor.fetchone()[0])
    except :
        pass

    return count


def get_number_of_classes() :
    count = "0"
    try :
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Execute the count query
        cursor.execute("SELECT COUNT(*) FROM classes")
        count = str(cursor.fetchone()[0])
    except :
        pass

    return count



def add_row_in_tables_quick_payment(window, list_of_settings):

    #u wont believe how much i spent for those 4 lines, I almost pulled the trigger
    #-------------saves in database--------------
    add_payment(1, list_of_settings[2], list_of_settings[3], list_of_settings[4], list_of_settings[5])
    #--------------------------------------------

    #-------------refresh the payment page--------------
    new_page = window.payments_page()
    window.stacked_widget.removeWidget(window.stacked_widget.widget(4))
    window.stacked_widget.insertWidget(4, new_page)
    #---------------------------------------------------



def add_row_in_tables_students(window, list_of_settings):

    #-------------saves in database--------------
    add_student(list_of_settings[0], list_of_settings[1], list_of_settings[2], list_of_settings[3], list_of_settings[4])
    #--------------------------------------------

    #-------------refresh the payment page--------------
    new_page = window.students_page()
    window.stacked_widget.removeWidget(window.stacked_widget.widget(4))
    window.stacked_widget.insertWidget(1, new_page)
    #---------------------------------------------------


def add_row_in_tables_teachers(window, list_of_settings):

    #-------------saves in database--------------
    add_teacher(list_of_settings[0], list_of_settings[1], list_of_settings[2], list_of_settings[3], list_of_settings[4])
    #--------------------------------------------

    #-------------refresh the payment page--------------
    new_page = window.teachers_page()
    window.stacked_widget.removeWidget(window.stacked_widget.widget(4))
    window.stacked_widget.insertWidget(2, new_page)
    #---------------------------------------------------


if __name__ == "__main__" :
    
    print('asdadsa')


