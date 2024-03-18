import logging


class Logger:
    def __init__(self) -> None:
        logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    @staticmethod
    def log_bot_restart() -> None:
        logging.info(msg="Запуск Бота PythonMummy")

    @staticmethod
    def log_user_add(user_chat_id: int, user_name: str, user_avatar: str) -> None:
        logging.info(msg=f"Регистрация Пользователя user_chat_id: {user_chat_id}, user_name: {user_name}, user_avatar: "
                     f"{user_avatar}")

    @staticmethod
    def log_see_top(user_chat_id: int, user_name: str, user_avatar: str) -> None:
        logging.info(msg=f"Просмотрел TOP user_chat_id: {user_chat_id}, user_name: {user_name}, user_avatar: "
                     f"{user_avatar}")

    @staticmethod
    def log_buy_item(user_chat_id: int, user_name: str, user_avatar: str, item_id: int) -> None:
        logging.info(msg=f"Купил Предмет {item_id}, user_chat_id: {user_chat_id}, user_name: {user_name}, user_avatar: "
                     f"{user_avatar}")

    @staticmethod
    def log_send_suggestion(user_chat_id: int, user_name: str, user_avatar: str) -> None:
        logging.info(msg=f"Отправил Предложение user_chat_id: {user_chat_id}, user_name: {user_name}, user_avatar: "
                     f"{user_avatar}")

    @staticmethod
    def log_rm_error(filename: str, exception: Exception) -> None:
        logging.error(msg=f"Ошибка Удаления Файла Из YADISK. Filename = {filename}. Exception - {exception}")

    @staticmethod
    def log_upload_error(dirr: str, filename: str, exception: Exception) -> None:
        logging.error(msg=f"Ошибка Загрузки Файла В YADISK. Filename = {filename}; Dir = {dirr}. Exception - {exception}")

    @staticmethod
    def log_download_error(dirr: str, filename: str, exception: Exception) -> None:
        logging.error(msg=f"Ошибка Скачивания Файла Из YADISK. Filename = {filename}; Dir = {dirr}. Exception - {exception}")

