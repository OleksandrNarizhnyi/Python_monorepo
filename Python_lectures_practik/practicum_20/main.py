# Задача: порекомендовать фильмы в определенной категории.
#
# Напишите программу, которая запрашивают информацию у пользователя,
# делает запросы в базу данных и выводит результат. Работаем с базой данных фильмов Sakila.

# При запуске программы выводится список категорий (номер и название категории)
# Пользователь может ввести номер категории
# Программа выводит все фильмы в данной категории, но не более 10 фильмов.
# О фильме выводится следующая информация: название, год выпуска, описание.

import pymysql
from query_manager import QueryHandler
from pymysql.cursors import DictCursor


dbconfig = {
    'host': 'ich-edit.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'ich1_password_ilovedbs',
    'database': 'Sakila',
    'charset': 'utf8mb4',
    'cursorclass': DictCursor
    }

def task1(dbconfig: dict, **params):
    query_handler = QueryHandler(dbconfig)

    try:
       [print(row.get('category_id'), row.get('name'), sep=' : ') for row in query_handler.get_all_category()]
       user_input = int(input("Enter category id: "))
       [print(row.get('title'), row.get('release_year'), row.get('description'), sep=' : ') for row in
        query_handler.get_film_by_category_id(user_input)]
    except pymysql.Error as e:
        print(f"SQLError-{e}")
    except Exception as e:
        print("Error")

# user_input = int(input("Enter category id: "))
# def task2(dbconfig: dict, category_id= input("Enter category id: "), **params ):
#     query_handler = QueryHandler(dbconfig)
#
#     try:
#        [print(row.get('title'), row.get('release_year'), row.get('description'), sep=' : ') for row in query_handler.get_film_by_category_id(user_input)]
#     except pymysql.Error as e:
#         print(f"SQLError-{e}")
#     except Exception as e:
#         print("Error")

if __name__ == "__main__":
    task1(dbconfig)
