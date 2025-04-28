import sqlite3



def creates_students_table ():

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        date_of_birth DATE NOT NULL,
        phone_number VARCHAR(10) NOT NULL,
        academic_year VARCHAR(50) NOT NULL,
        residance VARCHAR(50) NOT NULL
        
    )
    """)

    conn.commit()
    cursor.close()


def creates_teachers_table() :

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (

        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        name VARCHAR(50) NOT NULL,
        date_of_birth DATE NOT NULL,
        subject VARCHAR(50),
        phone_number VARCHAR(10) NOT NULL,
        residance VARCHAR(50)
    )
    """)
    conn.commit()
    cursor.close()



def creates_classes_table ():

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id INT NOT NULL REFERENCES teachers(id) ON DELETE CASCADE,
        subject VARCHAR(50) NOT NULL,
        academic_year VARCHAR(50),
        room VARCHAR(50) NOT NULL,
        period VARCHAR(50) NOT NULL,
        price INT NOT NULL,
        teacher_percentage INT NOT NULL
    )
    """)

    conn.commit()
    cursor.close()


def creates_enrollment_table ():

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollment(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INT NOT NULL REFERENCES students(id) ON DELETE CASCADE,
        classe_id INT NOT NULL REFERENCES classe(id) ON DELETE CASCADE,
        subscription_date DATE

    )
    """)

    conn.commit()
    cursor.close()



def creates_payments_table ():

    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        enrollment_id INTEGER NOT NULL,
        amount INT NOT NULL,
        marked_date DATE,
        time_method VARCHAR(50), 
        status TEXT

    )
    """)

    # time_method == how he is going to pay (mounthly / by number of attendance)

    conn.commit()
    cursor.close()



def add_student(name, date_of_birth, phone_number, academic_year, residance):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students (name, date_of_birth, phone_number, academic_year, residance) VALUES (?, ?, ?, ?, ?)", (name, date_of_birth, phone_number, academic_year, residance))


    conn.commit()
    cursor.close()


def add_teacher(name, date_of_birth, subject, phone_number, residance):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO teachers (name, date_of_birth, subject, phone_number, residance) VALUES (?, ?, ?, ?, ?)", (name, date_of_birth, subject, phone_number, residance))


    conn.commit()
    cursor.close()


def add_classe(teacher_id , subject, academic_year, room, period, price, teacher_percentage):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO classes (teacher_id , subject, academic_year, room, period, price, teacher_percentage) VALUES (?, ?, ?, ?, ?, ?, ?)", (teacher_id , subject, academic_year, room, period, price, teacher_percentage))


    conn.commit()
    cursor.close()



def add_enrollment(student_id , classe_id, subscription_date):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO enrollment(student_id , classe_id, subscription_date) VALUES (?, ?, ?)", (student_id , classe_id, subscription_date))


    conn.commit()
    cursor.close()



def add_payment(enrollment_id, amount, marked_date, mounth, status):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO payments(enrollment_id, amount, marked_date, time_method, status) VALUES (?, ?, ?, ?, ?)", (enrollment_id, amount, marked_date, mounth, status))


    conn.commit()
    cursor.close()







if __name__ == "__main__":
    for i in range(66): 

        add_teacher('حمزة غراسي', '1990', 'فيزياء', '066988557', 'الخربة')

    for i in range(300): 

        add_student('بوطواطو يوسف', '2005', '066988557', 'ثاني ثانوي','حي قصر الماء')

    for i in range(20): 

        
        add_classe(1, 'رياضيات', '8:30 - 10:00', 'اولى متوسط','حي قصر الماء','3000','20')
        add_enrollment(1,1,'20/11/2005')
        add_payment(1,1000,'20/11/2005','مارس','مدفوع')
