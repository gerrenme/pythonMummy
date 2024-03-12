import telebot
import os

from database_calls import DatabaseCaller
from message_creator import MessageCreator
from static_service import StaticSrvice

from config import telebot_key


class PythonMummyBot:
    def __init__(self):
        self.__bot: telebot.TeleBot = telebot.TeleBot(telebot_key)
        self.db_connect: DatabaseCaller = DatabaseCaller()
        self.message_creator: MessageCreator = MessageCreator()
        self.static_service: StaticSrvice = StaticSrvice()

        @self.__bot.message_handler(commands=["start"])
        def send_start_message(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id

            is_user: bool = self.db_connect.check_user(user_chat_id=user_chat_id)
            if is_user:
                self.__bot.send_message(user_chat_id, text="Ты уже зарегистрирован в PythonMummy. "
                                                           "Тебе уже доступны все привилегии нашего бота :)")
            else:
                self.__bot.send_message(user_chat_id,
                                        text="Укажи имя твоего аватара. Имя должно соответствовать следующим "
                                             "параметрам: длина от 4 до 32-х символов включительно, имя состоит "
                                             "только из латинских букв, имя должно быть уникальным")
                self.__bot.register_next_step_handler(message, self.add_user_avatar)

        @self.__bot.message_handler(commands=["pic"])
        def send_pic(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id
            current_dir: str = os.getcwd()
            photos: list[telebot.types.InputMediaPhoto] = []

            for filename in os.listdir(current_dir + "/../chapter/PC00/"):
                if filename.endswith("PC00.png"):
                    print(filename)
                    photo = open(os.path.join(current_dir, filename), 'rb')
                    photos.append(telebot.types.InputMediaPhoto(photo))
                    photo.close()

                if photos:
                    self.__bot.send_media_group(user_chat_id, media=photos)
                    print("sended")
            return

        @self.__bot.message_handler(commands=["get_progress"])
        def get_progress(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id
            res: tuple = self.db_connect.get_user_progress(user_chat_id=user_chat_id)
            user_progress: dict[str, str] = {
                "Course": res[0],
                "InterviewTask": res[1],
                "Notebook": res[2]
            }

            self.__bot.send_message(user_chat_id, self.message_creator.create_progress_message(
                course=user_progress["Course"],
                interview_task=user_progress["InterviewTask"],
                notebook=user_progress["Notebook"]))
            return

        @self.__bot.message_handler(commands=["top"])
        def get_leaderboard(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id
            user_avatar: str = self.db_connect.get_user_avatar(user_chat_id=user_chat_id)[0]

            res: list = list(self.db_connect.get_top_users())
            top_users: list[str] = [f"{t[0]} {t[1]} lvl with {t[2]} exp" for t in res]

            top_users_message: str = ("Представляем топ-10 пользователей PythonMummy:\n\n🎶" + "\n🎶".join(top_users) +
                                      "\n\nДо окончания гонки осталось n дней")

            self.__bot.send_message(user_chat_id, text=top_users_message)

            if user_avatar in top_users_message:
                self.__bot.send_message(user_chat_id, text="Поздравляем! Ты уверенно входишь в топ-10 пользователей🎉 "
                                                           "\nПо окончанию гонки ты получишь приятный приз :)")
            else:
                self.__bot.send_message(user_chat_id, text="Ты пока не взобрался в топ-10 пользователей бота, но у "
                                                           "тебя все впереди! Мы верим в тебя!")
            return

        @self.__bot.message_handler(commands=["store"])
        def

        @self.__bot.message_handler(commands=["store"])
        def get_store_data(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id
            store_link: str = "https://disk.yandex.ru/i/gRVYI2aP60fTuw"
            self.__bot.send_message(user_chat_id, text=f"Наш магазин предоставляет широкий ассортимент, ознакомиться "
                                                       f"с которым можно по ссылке {store_link}.")

            return

        # TODO. Прописать хендлер сообщения и зачисление предмета. Также стоит проработать логику хранения снаряжения
        @self.__bot.message_handler(commands=["buy"])
        def process_buy_request(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id
            user_balance: int = int(self.db_connect.get_user_balance(user_chat_id=user_chat_id)[0])
            possible_items: tuple = self.db_connect.get_possible_items(user_balance=user_balance)

            self.__bot.send_message(user_chat_id, text="Ниже приведен список вещей, которые ты можешь купить: \n\n● " +
                                                       "\n● ".join([f"{t[0]} — {t[1]} Gold" for t in possible_items])
                                    + f"\n\n Твой баланс {user_balance} Gold. "
                                      f"Введи название предмета, который хочешь купить")

            return

        @self.__bot.message_handler(commands=["suggest"])
        def create_suggestion(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id

            self.__bot.send_message(user_chat_id, text="Введите ваше предложение по улучшению PythonMummy")
            self.__bot.register_next_step_handler(message, add_suggestion)

            return

        @self.__bot.message_handler(content_types=["text"])
        def get_text_content(message: telebot.types.Message) -> None:
            self.__bot.send_message(message.from_user.id, text="crigne text given")
            return

        def add_suggestion(message: telebot.types.Message) -> None:
            user_chat_id: int = message.from_user.id
            user_avatar: str = self.db_connect.get_user_avatar(user_chat_id=user_chat_id)[0]
            user_suggestion: str = message.text.strip().lower()

            self.db_connect.add_suggestion(user_avatar=user_avatar, user_suggestion=user_suggestion)
            self.__bot.send_message(user_chat_id, text="Предложение успешно добавлено! Спасибо за помощь!")

            return

    def add_user_avatar(self, message: telebot.types.Message) -> None:
        user_avatar: str = message.text.strip()
        user_chat_id: int = message.from_user.id
        user_name: str = message.from_user.username

        if (self.static_service.validate_name(name=user_avatar)
                and not self.db_connect.check_avatar(user_avatar=user_avatar)):
            self.db_connect.add_user(user_chat_id=user_chat_id, user_name=user_name, user_avatar=user_avatar)
            self.__bot.send_message(user_chat_id, text="Теперь ты являешься одним из последователей PythonMummy!")

        else:
            self.__bot.send_message(user_chat_id, text="К сожалению, вы указали имя, которое не соответствует "
                                                       "параметрам, либо такое имя уже занято. Повтори операцию "
                                                       "регистрации снова через команду /start")

    def run(self) -> None:
        self.__bot.polling()


if __name__ == "__main__":
    mummy: PythonMummyBot = PythonMummyBot()
    mummy.run()
