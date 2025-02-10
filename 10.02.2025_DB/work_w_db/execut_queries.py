from pymysql.cursors import DictCursor
from db_connector import DBConection

class ExecuteQueries:
    dbconfig = {
        'host': 'ich-edit.edu.itcareerhub.de',
        'user': 'ich1',
        'password': 'ich1_password_ilovedbs',
        'database': '160924_social_blogs',
        'charset': 'utf8mb4',
        'cursorclass': DictCursor
    }
    @classmethod
    def _get_db_config(cls):
        return cls.dbconfig

    def __init__(self):
        self._dbconfig = self._get_db_config()

    def get_moderators(self, role=2):
        with DBConection(**self._dbconfig) as manager:
            manager.execute(
                """
                    SELECT last_name, email, rating, role_id
                    FROM User
                    WHERE role_id = %s
                """,
                (role,)
            )
            moderators = manager.fetchall()

            return moderators