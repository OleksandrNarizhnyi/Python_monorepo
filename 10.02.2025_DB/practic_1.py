# Написать программу, которая запрашивает у пользователя возраст и выводит все строки
# таблицы users, где возраст больше указанного.

import pymysql
from pymysql.cursors import DictCursor

dbconfig = {
'host': 'ich-edit.edu.itcareerhub.de',
'user': 'ich1',
'password': 'ich1_password_ilovedbs',
'database': '160924_social_blogs',
'charset': 'utf8mb4',
'cursorclass': DictCursor
}

connector = pymysql.connect(**dbconfig)
cursor = connector.cursor()

cursor.execute(
    """
    select * from User
    where role_id = %s
    """,
    (2,)
    )

required = cursor.fetchall()

for r in required:
    print(r)

cursor.close()
connector.close()