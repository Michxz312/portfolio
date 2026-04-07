import pymysql


def create_connection():
    return pymysql.connect(
        host="localhost",
        db="mydb",
        user="root",
        password="",
        charset="utf8",
        cursorclass = pymysql.cursors.DictCursor
    )

def insert_employees(employee):
    con = create_connection()
    cursor = con.cursor()
    sql = "INSERT INTO employees (skill_level, training, salary) INTO VALUES(%s,%s,%s,%s)"
    for e in employee:
        e["training_level"] = ','.join(e['training_level'])
    cursor.execute(sql, (employee))
    con.commit()
    cursor.close()
    con.close()