import psycopg2
from config import db_host, db_name, db_user, db_password


class DatabaseCaller:
    def __init__(self) -> None:
        self.__connection: psycopg2.connect = psycopg2.connect(host=db_host, user=db_user,
                                                               password=db_password, database=db_name)
        self.__connection.autocommit = True

    def add_user(self, user_chat_id: int, user_name: str) -> bool:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"SELECT * "
                           f"FROM Users AS us "
                           f"WHERE us.user_chat_id = {user_chat_id};")
            result: list[tuple] = cursor.fetchone()

            if result is None:
                with self.__connection.cursor() as cursor:
                    cursor.execute(f"INSERT INTO Users(user_name, user_chat_id) "
                                   f"VALUES('{user_name}', {user_chat_id});")
                    return True

        return False

    def get_user_progress(self, user_chat_id: int) -> tuple:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"SELECT us.user_chapter_id, us.user_task_id, us.user_notebook_id "
                           f"FROM Users AS us "
                           f"WHERE us.user_chat_id = {user_chat_id};")
            return cursor.fetchone()

    def get_user_data(self, user_chat_id: int) -> tuple:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"SELECT * "
                           f"FROM Users AS us "
                           f"WHERE us.user_chat_id = {user_chat_id};")
            return cursor.fetchone()

    def get_top_users(self) -> tuple:
        with self.__connection.cursor() as cursor:
            cursor.execute(f"SELECT us.user_name, us.user_level, us.user_exp "
                           f"FROM Users AS us "
                           f"ORDER BY us.user_exp DESC "
                           f"LIMIT 10;")

            return cursor.fetchall()


