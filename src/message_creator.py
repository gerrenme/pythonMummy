from random import choice
from config import facts_about_python, task_lib


class MessageCreator:
    @staticmethod
    def create_progress_message(course: str, interview_task: str, notebook: str) -> str:
        # не двиигать. у многострочной f-строки конченная табуляция, пришлось так
        message: str = (f"""Your score so far: 
                \b\bCourse {course} - In progress☯
                \b\bInterview Task {interview_task} - In progress☯
                \b\bNotebook {notebook} - In progress☯︎ """)

        return message

    def create_leaderboard_list(self):
        pass

    @staticmethod
    def create_random_fact() -> str:
        message: str = f"Интересный факт №{choice(facts_about_python)} Прикольно, правда?"

        return message

    @staticmethod
    def create_interview_list(interviews: dict) -> str:
        message: list[str] = ["Ниже приведен ваш список задач:\n\n"]
        for name, val in interviews.items():
            message.append(f"{'🟥' if val == 0 else '🟢'} {name} -- {task_lib[name][0]}. {task_lib[name][1]}")

        message.append(f"Вы решили {round(sum(interviews.values()) / len(interviews))}% задач. Введите номер задачи, "
                       f"которую хотите решить")
        return "\n".join(message)
