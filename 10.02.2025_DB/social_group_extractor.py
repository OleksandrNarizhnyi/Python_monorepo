# "Получить новости всех авторов"
# "Получить все роли"
# "Получить email адреса авторов с рейтингом выше 4"

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

def get_news(manager):
    manager.execute(
        """
        select title, role_id from News as n
        join User as u
        on n.author_id = u.id and u.role_id = 3
        
        """
    )
    author_news = manager.fetchall()
    return author_news

def get_roles(manager):
    manager.execute(
        """
        select name from Role
        """
    )
    all_roles = manager.fetchall()
    return all_roles

def get_emails(manager):
    manager.execute(
        """
        select email from User
        where role_id = 3 and rating > 4
        """
    )
    autor_emails = manager.fetchall()
    return autor_emails


actions = {
    "Получить новости всех авторов": get_news,
    "Получить все роли": get_roles,
    "Получить email адреса авторов с рейтингом выше 4": get_emails
}

req_action = input("Введите необходимое действие: ").strip().capitalize()

data = actions.get(req_action)
if not data:
    print("Недопустимое значение")
else:
    for r in data(cursor):
        print(r)

cursor.close()
connector.close()