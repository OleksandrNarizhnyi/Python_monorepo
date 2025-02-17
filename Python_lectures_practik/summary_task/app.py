import pymysql

from db_queries import QueryHandler
from pymysql.cursors import DictCursor

dbconfig = {
             'host': 'ich-edit.edu.itcareerhub.de',
             'user': 'ich1',
             'password': 'ich1_password_ilovedbs',
             'database': '160924_social_blogs',
             'charset': 'utf8mb4',
             'cursorclass': DictCursor
         }

def main(dbconfig, action: str, **params):
    query_handler = QueryHandler(dbconfig)
    dict_actions = {
        "get_all_roles": query_handler.get_all_roles,
        "get_role_id_by_name": query_handler.get_role_id_by_name,
        "get_field_name_new": query_handler.get_field_name_new,
        "get_user_query": query_handler.get_user_query
    }

    try:
        key =  action.lower()
        if dict_actions.get(key):
            result = dict_actions.get(key)(**params)
            return result
        return "Действие или таблица не существует!"
    except pymysql.Error as e:
        print(f"SQLError-{e}")
    except Exception as e:
        print("Error")


user_query1 = main(dbconfig, "get_user_query",  t_name= "User")
#user_query = main(dbconfig, "get_user_query",  t_name= "User", operator = "=", value = 3, field_name = "id")

#res_all_roles = main(dbconfig, "get_all_roles",  t_name= "Role")

# res_all_roles = main(dbconfig, "Role", "get_all_roles")
# res_id_by_name = main(dbconidfig, "Role", "get_role_id_by_name", name="admin")
# print(res_all_roles)
# print(res_id_by_name)

# get_name = main(dbconfig,  "get_field_name", t_name= "Role")
#
# get_name1 = main(dbconfig,  "get_field_name", t_name= "User")
#
# get_field_name_new = main(dbconfig,  "get_field_name_new", t_name= "User")

# print(res_all_roles)
# print("-"*100)
# print(get_name1)
# print("-"*100)
# print(get_field_name_new)
# print("-"*100)
for elem in user_query1:
    print(elem)