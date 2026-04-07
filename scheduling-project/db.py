import pymysql


connection = pymysql(
    host="localhost",
    db="mydb",
    user="root",
    password="",
    charset="utf8",
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connection.cursor()

