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

# ACID - A -> (Атомарность)
# commit() -> если всё прошло хорошо - коммитим
# rollback() -> если хоть одна операция в транзакции не пройдёт - откатываем всё назад на момент последнего состояния базы данных

moderator_email = "tammy54@yahoo.com"
author_email = "qhayes@gmail.com"
moderator = "moderator"
author = "author"

try:
    cursor.execute(
        """SELECT id
        FROM Role
        WHERE name in (%s, %s)""",
        (moderator, author)
    )

    roles = cursor.fetchall()  # [{...}, {...}]
    print(roles)
    author_role_id = roles[1]['id']
    moderator_role_id = roles[0]['id']

    cursor.execute(
        """
            UPDATE User
            SET role_id = %s
            WHERE email = %s
        """,
        (author_role_id, moderator_email)
    )

    cursor.execute(
        """
            UPDATE User
            SET role_id = %s
            WHERE email = %s
        """,
        (moderator_role_id, author_email)
    )

    if cursor.rowcount == 0:
        raise ValueError("Update failed; no rows affected.")
    connector.commit()

    cursor.execute(
        """
            SELECT email, role_id
            FROM User
            WHERE email IN (%s, %s)
        """,
        (moderator_email, author_email)
    )

    data = cursor.fetchall()

    print(data)

except pymysql.Error as e:
    print("[Database ERROR]:", e)
    connector.rollback()
except Exception as e:
    print("[Exception]:", e)
    connector.rollback()
finally:
    cursor.close()
    connector.close()