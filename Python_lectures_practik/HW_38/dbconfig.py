from pymysql.cursors import DictCursor

dbconfig = {
             'host': 'ich-edit.edu.itcareerhub.de',
             'user': 'ich1',
             'password': 'ich1_password_ilovedbs',
             'database': '160924_social_blogs',
             'charset': 'utf8mb4',
             'cursorclass': DictCursor
         }