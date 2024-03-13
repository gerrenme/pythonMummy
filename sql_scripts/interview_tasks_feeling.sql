INSERT INTO InterviewTasks (task_id, task_text, task_answer_1, task_answer_2, task_answer_3, task_complexity, task_money_award, task_exp_award)
VALUES
('PIT1', 'Что такое docstring?',
    'строка, которая идет сразу после определения функции, метода или класса, и содержит информацию о том, что делает код, аргументы, возвращаемые значения и другие детали',
    'это строка документации, написанная внутри исходного кода программы на языке программирования, обычно располагается в начале функции, модуля или класса. Она предназначена для объяснения назначения, использования и деталей реализации соответствующего объекта кода.',
    'это строка документации, которая описывает, что делает функция, метод, модуль или класс Python. Данная строка располагается в начале определения объекта и используется для генерации документации автоматически.',
    'easy', 10, 10),

('PIT2', 'Что такое lambda-функция?',
    'Lambda-функция - это специальный вид функции в языке программирования, который позволяет создавать функции без необходимости объявления их с именем.',
    'Lambda-функция - это способ определения и использования функции в одной строке кода без явного указания имени, часто используемый для кратких операций и обработки коллекций данных.',
    'Lambda-функция - это анонимная функция в программировании, которая обычно используется для создания простых функций прямо в месте их вызова.',
    'easy', 10, 10),

('PIT3', 'В чем различия между итератором и генератором?',
    'Генератор создает значения при запросе, в то время как итератор возвращает уже существующие значения.',
    'Генератор использует ключевое слово yield для возврата значений, а итератор реализует методы iter() и next().',
    'Генератор автоматически сохраняет состояние выполнения функции, тогда как итератор требует явного хранения состояния.',
    'medium', 18, 18),

('PIT4', 'Что такое *args и **kwargs в определении функции?',
    '*args позволяет передавать произвольное количество позиционных аргументов в функцию в виде кортежа.',
    '**kwargs позволяет передавать произвольное количество именованных аргументов в функцию в виде словаря.',
    '',
    'medium', 15, 15),

('PIT5', 'Python полностью поддерживает ООП?',
    'Python поддерживает основные принципы ООП, такие как наследование, инкапсуляция и полиморфизм.',
    'В Python все данные представлены объектами, что соответствует основным концепциям ООП.',
    'Python позволяет создавать классы, объекты, методы и атрибуты, что делает его полноценным языком для объектно-ориентированного программирования.',
    'hard', 25, 25);