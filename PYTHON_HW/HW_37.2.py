# В базе данных ich_edit три таблицы. Users с полями (id, name, age),
# Products с полями (pid, prod, quantity) и Sales с полями (sid, id, pid).
# Программа должна вывести все имена из таблицы users,
# дать пользователю выбрать одно из них и вывести все покупки этого пользователя

import pymysql
try:
    dbconfig = {
            'host': 'ich-edit.edu.itcareerhub.de',
            'user': 'ich1',
            'password': 'ich1_password_ilovedbs',
            'database': 'ich_edit',
            'charset': 'utf8mb4'

        }
    connector = pymysql.connect(**dbconfig)
    cursor = connector.cursor()

    def names_from_users(cursor):
        cursor.execute(
            """
            SELECT name FROM Users
            """
            )
        names = cursor.fetchall()
        for name in names:
            print(name)
        select_name = input("Введите имя из списка выше: ")
        cursor.execute(
            """
            SELECT prod, quantity FROM Products as p
            join Sales as s
            on s.pid = p.pid 
            join Users as u
            on u.id = s.id  
            where u.name = %s
            """, (select_name,)
        )
        results = cursor.fetchall()
        return results

    for sales in names_from_users(cursor):
        print(sales)


except pymysql.MySQLError as e:
    print("Wrong connection", e)
finally:
    if "connector" in locals() :
        cursor.close()
        connector.close()