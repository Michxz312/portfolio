import pymysql
import os

def create_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        database="mydb",
        password=os.getenv("MYSQL_PASSWORD"),
        charset="utf8",
        cursorclass = pymysql.cursors.DictCursor
    )

def insert_students(students):
    con = create_connection()
    cursor = con.cursor()
    sql = "INSERT INTO students (id, gender, international, preference) VALUES(%s,%s,%s,%s)"
    data = []
    print(students)
    for s in students:
        data.append((s['student_id'], s['gender'], s['international'], ','.join(map(str, s['preference']))))
    cursor.executemany(sql, data)
    con.commit()
    cursor.close()
    con.close()

def insert_courses(courses):
    con = create_connection()
    cursor = con.cursor()
    sql = "INSERT INTO courses (id, max) VALUES(%s,%s)"
    data = []
    for c in courses:
        data.append((
            c['course_id'],
            c['max']
        ))
    cursor.executemany(sql, data)
    con.commit()
    cursor.close()
    con.close()

def get_students():
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    students = cursor.fetchall()
    cursor.close()
    con.close()
    return students

def get_courses():
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM courses"
    cursor.execute(sql)
    courses = cursor.fetchall()
    cursor.close()
    con.close()
    return courses

def reset_all():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM students")
    cursor.execute("DELETE FROM courses")
    con.commit()
    cursor.close()
    con.close()

def init():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY,
        gender INT,
        international INT,
        preference TEXT
    )""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INT PRIMARY KEY,
        max INT
    )""")
    con.commit()
    cursor.close()
    con.close()