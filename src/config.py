db_host: str = "127.0.0.1"
db_user: str = "gerrenme"
db_password: str = "1"
db_name: str = "pythonMummy"

admin_password: str = "1"
telebot_key: str = "6861912111:AAG1HmkE2cRhhpgNAAnAl4aLJNiP_7nWlLA"

system_messages: dict[str, str] = {"already_registered": "Ты уже зарегистрирован в PythonMummy. "
                                                         "Тебе уже доступны все привилегии нашего бота :)",
                                   "name_rules": "Укажи имя твоего аватара. Имя должно соответствовать следующим "
                                                 "параметрам: длина от 4 до 32-х символов включительно, имя состоит "
                                                 "только из латинских букв, имя должно быть уникальным",
                                   "menu_roadmap": "Ты находишься в главном меню PythonMummy. Отсюда ты можешь "
                                                   "попасть в: \n\n● Магазин\n● Курс\n● Ноутбуки\n● Вопросы на "
                                                   "собеседования\n● Лидерборд\nz",
                                   "grats_top_10": "Поздравляем! Ты уверенно входишь в топ-10 пользователей🎉 "
                                                   "\nПо окончанию гонки ты получишь приятный приз :)",
                                   "not_top_10": "Ты пока не взобрался в топ-10 пользователей бота, но у "
                                                 "тебя все впереди! Мы верим в тебя!",
                                   "store_present": "Наш магазин предоставляет широкий ассортимент, ознакомиться с "
                                                    "которым можно по ссылке",
                                   "get_suggestion": "Введите ваше предложение по улучшению PythonMummy",
                                   "success_suggestion": "Предложение успешно добавлено! Спасибо за помощь!",
                                   "wrong_name": "Предложение успешно добавлено! Спасибо за помощь!",
                                   "grats_new_user": "Теперь ты являешься одним из последователей PythonMummy!",
                                   "cringe_text": "crigne text given", }

facts_about_python: list[str] = [
        "1. Динамическая типизация и утиная типизация: В Python используется динамическая типизация, что означает, "
        "что тип переменной определяется автоматически во время выполнения программы. Это может быть как "
        "преимуществом, так и недостатком, в зависимости от контекста. Также Python поддерживает утиную типизацию, "
        "что означает, что важнее интерфейс объекта, чем его конкретный тип. Это позволяет писать более гибкий и "
        "модульный код.",
        "2. Генераторы и итераторы: Python предоставляет мощные инструменты для работы с последовательностями данных "
        "через генераторы и итераторы. Генераторы позволяют создавать последовательности данных ленивым образом, "
        "что экономит память и улучшает производительность программы.",
        "3. Декораторы: Декораторы - это мощный инструмент в Python, позволяющий изменять поведение функций или "
        "классов, не изменяя их исходный код. Они широко используются для реализации паттернов проектирования, "
        "валидации данных, логирования и других аспектов разработки.",
        "4. Множественное наследование и миксины: Python поддерживает множественное наследование классов, "
        "что позволяет классам наследовать атрибуты и методы нескольких родительских классов. Это может быть полезным "
        "для создания модульной иерархии классов. Также Python поддерживает концепцию миксинов, которая позволяет "
        "добавлять функциональность к классам без изменения их исходного кода.",
        "5. Гибкая обработка ошибок: Python предоставляет механизмы для обработки исключений, позволяющие "
        "программистам элегантно обрабатывать ошибки и исключения в своих программах. Это помогает улучшить "
        "отказоустойчивость и надежность программного обеспечения.",
        "6. Функциональное программирование: Хотя Python не является чистым функциональным языком программирования, "
        "он поддерживает функциональные концепции, такие как анонимные функции (lambda), высшие порядковые функции, "
        "замыкания и рекурсия. Это позволяет писать более краткий и выразительный код.",
        "7. Средства метапрограммирования: Python предоставляет средства метапрограммирования, позволяющие "
        "программистам модифицировать программу во время её выполнения. Это включает в себя использование "
        "декораторов, метаклассов, функций eval и exec, а также рефлексию.",
        "8. Управление памятью: Python использует автоматическое управление памятью через механизм сборки мусора. Это "
        "означает, что программистам не нужно явно освобождать память после использования объектов, что упрощает "
        "процесс разработки и уменьшает вероятность утечек памяти.",
        "9. Богатая экосистема библиотек: Python имеет огромное количество сторонних библиотек и фреймворков, "
        "покрывающих практически все области программирования. Это позволяет программистам быстро создавать сложные "
        "приложения, используя готовые компоненты.",
        "10. Интеграция с другими языками: Python легко интегрируется с кодом, написанным на других языках "
        "программирования, таких как C/C++, Java и JavaScript. Это позволяет использовать существующий код и "
        "библиотеки в Python-проектах и наоборот."
]

