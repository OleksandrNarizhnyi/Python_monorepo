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

class DBConection:
    def __init(self,**kwargs):
        self.connection = pymysql.connect(**kwargs)
        self.cursor = self.connection.cursor()

    def __enter__(self): # момент входа в блок кода
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            try:
                self.connection.commit()
            except Exeption as e:
                print("[Commit error]:", e)
                self.connection.rollback()

        else:
            self.connection.rollback()

        self.cursor.close()
        self.connection.close()