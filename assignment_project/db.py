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
    for s in students:
        id, gender, international, preference_list = s
        preference = ','.join(map(str, preference_list))
        data.append((id, gender, international, preference))
    cursor.executemany(sql, data)
    con.commit()
    cursor.close()
    con.close()

def insert_courses(courses):
    con = create_connection()
    cursor = con.cursor()
    sql = "INSERT INTO courses (id, max) VALUES(%s,%s)"
    cursor.executemany(sql, courses)
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