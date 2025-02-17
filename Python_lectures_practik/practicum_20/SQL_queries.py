class CategoryQueries:
    GET_ALL = "SELECT category_id, name from category"
    GET_NAME_BY_ID = "SELECT name from category where category_id = %s"


class FilmQueries:
    GET_ALL = "SELECT title, release_year, description from film"
    GET_ALL_BY_CATEGORY = """
    SELECT title, release_year, description 
    from film as f
    join film_category as f_c
    on f.film_id = f_c.film_id
    and f_c.category_id = %s
    """
