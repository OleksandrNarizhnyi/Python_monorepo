from Python_lectures_practik.practicum_20.SQL_queries import CategoryQueries, FilmQueries
from db_conector import DBConnection

class QueryHandler(DBConnection):
    def __init__(self, dbconfig):
        super().__init__(dbconfig)

    def get_all_category(self):
        cursor = self.get_cursor()
        cursor.execute(CategoryQueries.GET_ALL)
        record = cursor.fetchall()
        return record

    def get_categoryname_by_id(self, category_id: int):
        cursor = self.get_cursor()
        cursor.execute(CategoryQueries.GET_NAME_BY_ID, (category_id,))
        record = cursor.fetchone()
        if record:
            return record.get("name")
        return None

    def get_all_films(self):
        cursor = self.get_cursor()
        cursor.execute(FilmQueries.GET_ALL)
        record = cursor.fetchone()
        return record

    def get_film_by_category_id(self, category_id: int):
        cursor = self.get_cursor()
        cursor.execute(FilmQueries.GET_ALL_BY_CATEGORY, (category_id,))
        record = cursor.fetchone()
        return record
