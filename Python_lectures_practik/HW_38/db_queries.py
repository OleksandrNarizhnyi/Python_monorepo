from db_connection import DBConnector

class QueryHandler(DBConnector):
    def __init__(self, dbconfig):
        super().__init__(dbconfig)

    def get_all_roles(self, t_name):
        cursor = self.get_cursor()
        cursor.execute(f"select * from {t_name}")
        records = cursor.fetchall()
        return records

    def get_role_id_by_name(self, name):
        cursor = self.get_cursor()
        cursor.execute("""
        select id from Role
        where name = %s
        """, (name,))
        record = cursor.fetchone()
        if record:
            return record
        return None

    def get_field_name_new(self, t_name: str):
        cursor = self.get_cursor()
        cursor.execute(f"describe {t_name}")
        return [column['Field'] for column in cursor.fetchall()]


    def get_user_query(self, t_name: str):
        cursor = self.get_cursor()

        cursor.execute(f"DESCRIBE {t_name}")
        columns = [column['Field'] for column in cursor.fetchall()]
        print("Доступные имена полей:", columns)

        field_name = input("Введите поле из выше перечисленных : ")
        if field_name not in columns:
            print(f"Поле - '{field_name}' не существует в таблице - '{t_name}'.")
            return []

        operator = input("Введите оператор сравнения ['>', '<', '=', '<=', '>=']: ")
        if operator not in ['>', '<', '=', '<=', '>=']:
            print("Оператор не валиден! По умолчанию будет использован оператор '='")
            operator = '='

        value = input("Введите сравниваемое значение: ")

        try:
            value = int(value)
        except ValueError:
            print("Значение не валидно! Введите число.")
            return []

        query = f"select * from {t_name} where {field_name} {operator} %s"
        cursor.execute(query, (value,))

        return cursor.fetchall()
