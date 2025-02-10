import pymysql
from pymysql.cursors import DictCursor

dbconfig = {  # для mysql порт по умолчанию 3306
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'db': 'ich_edit',
    'charset': 'utf8mb4',
    'cursorclass':DictCursor
}

# connector = mysql.connector.connect(**dbconfig)
connector = pymysql.connect(**dbconfig)
cursor = connector.cursor()

# cursor.execute("SELECT * FROM users")
# data = cursor.fetchall()
#
# for user in data:
#     print(user)

name = 'USER 4'
age = 48

cursor.execute(
    "INSERT INTO users (name, age) VALUES (%s, %s)",
    (name, age)
)  # пока commit() явно не будет сделан - изменения будут "висеть" в объекте подключения

connector.commit()

cursor.execute(
    "SELECT * FROM users WHERE name = %s",
    (name,)
)

user_data = cursor.fetchone()
print(user_data)


cursor.close()
connector.close()