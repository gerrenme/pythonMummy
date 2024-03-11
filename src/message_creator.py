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
