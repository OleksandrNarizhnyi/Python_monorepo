

import pymysql

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

    def commit(self):
        try:
            self._connection.commit()
        except pymysql.Error as e:
            print(e.msg)
            self._connection.rollback()

    def get_connection(self):
        return self._connection

    def get_cursor(self):
        return self._cursor

    def close(self):
        if self._connection.open:
            self._cursor.close()
            self._connection.close()