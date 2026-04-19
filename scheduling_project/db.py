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

def insert_employees(employee):
    con = create_connection()
    cursor = con.cursor()
    sql = "INSERT INTO employees (skill_level, training, salary) VALUES(%s,%s,%s)"
    data = []
    for e in employee:
        skill, training_list, salary = e
        training = ','.join(map(str, training_list))
        data.append((skill, training, salary))
    cursor.executemany(sql, data)
    con.commit()
    cursor.close()
    con.close()

def insert_customer(customer):
    con = create_connection()
    cursor = con.cursor()
    sql = "INSERT INTO customers (day_label, shift, shift_demand) VALUES(%s,%s,%s)"
    cursor.executemany(sql, customer)
    con.commit()
    cursor.close()
    con.close()

def get_employee():
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM employees"
    cursor.execute(sql)
    employees = cursor.fetchall()
    cursor.close()
    con.close()
    return employees

def get_customer():
    con = create_connection()
    cursor = con.cursor()
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    customers = cursor.fetchall()
    cursor.close()
    con.close()
    return customers

def reset_all():
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("DELETE FROM employees")
    cursor.execute("DELETE FROM customers")
    con.commit()
    cursor.close()
    con.close()