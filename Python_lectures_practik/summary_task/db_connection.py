import pymysql

# dbconfig = {
#             'host': 'ich-edit.edu.itcareerhub.de',
#             'user': 'ich1',
#             'password': 'ich1_password_ilovedbs',
#             'database': '160924_social_blogs',
#             'charset': 'utf8mb4'
#             'cursorclass': DictCursor
#         }


class DBConnection:

    def __init__(self, dbconfig):
        self._dbconfig = dbconfig
        self._connection = self._set_connection()
        self._cursor = self._set_cursor()

    def _set_connection(self):
        connection = pymysql.connect(**self._dbconfig)
        return connection

    def _set_cursor(self):
        cursor = self._connection.cursor()
        return cursor

    def get_connection(self):
        return self._connection

    def get_cursor(self):
        return self._cursor

    def close(self):
        if self._connection.open:
            self._cursor.close()
            self._connection.close()