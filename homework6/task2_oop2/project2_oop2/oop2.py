"""
Task.

В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict
from typing import Union


class Homework:
    """Create Homework object."""

    def __init__(self, text: str, days_to_deadline: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=days_to_deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Check if there is time till deadline of current homework.

        Return True if the deadline has not expired, False otherwise.
        """
        return self.created + self.deadline > datetime.datetime.now()


class DeadlineError(Exception):
    """Raise when homework is inactive when its deadline has already ended."""

    pass


class NameSurnameCreation:
    """Create an instance of a person. Base class for Student and Teacher classes."""

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class HomeworkResult:
    """Contain information about homework result.

    Raise HomeworkError if a given homework is not a Homework class object.
    """

    def __init__(self, homework: Homework, solution: str) -> None:
        if not isinstance(homework, Homework):
            raise HomeworkTypeError("You gave not a Homework object")
        self.author = Student
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


class Student(NameSurnameCreation):
    """Create Student object."""

    @staticmethod
    def do_homework(
        home_work: Homework, result: str
    ) -> Union[HomeworkResult, DeadlineError]:
        """Checks is the deadline of the given homework expired or not.

        Return HomeworkResult class object if deadline hasn't expired yet, otherwise raise DeadlineError.
        """
        if home_work.is_active():
            return HomeworkResult(home_work, result)
        else:
            raise DeadlineError("You are late")


class HomeworkTypeError(Exception):
    """Raise if a given homework in HomeworkResult constructor is not a Homework class object."""

    pass


class Teacher(NameSurnameCreation):
    """Create Teacher object.

    Has class attribute - homework_done, which is a data structure with dictionary interface. All HomeworkResult
    objects are saved here after successful check_homework method applying.
    """

    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(task: str, days_to_do_task: int) -> Homework:
        """Creates an instance of Homework class object."""
        return Homework(task, days_to_do_task)

    @staticmethod
    def check_homework(homework_result: HomeworkResult) -> bool:
        """Check given homework result.

        Return True if homework solution consists of more than 5 symbols, otherwise return False. If True, homework
        solution is saved in homework_done data structure.
        """
        if len(homework_result.solution) > 5:
            Teacher.homework_done[homework_result.homework.text].add(
                homework_result.solution
            )
            return True
        return False

    @staticmethod
    def reset_results(homework: Homework = None) -> None:
        """Depending on a given argument, this method partly or fully remove results in homework_done data structure.

        If homework is not given as an argument, this method remove all information in homework_done data structure.
        Otherwise, it removes only results of a given homework.
        """
        if homework:
            Teacher.homework_done[homework.text].clear()
        else:
            Teacher.homework_done.clear()
