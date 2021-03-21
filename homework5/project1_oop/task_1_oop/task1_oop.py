"""
Task.

Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатает 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import Any


class Homework:
    """Create Homework objects."""

    def __init__(self, text: str, deadline: int) -> None:
        """Creates a class instance."""
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Check if there is time till deadline of current homework.

        Return True if the deadline has not expired, False otherwise.
        """
        return self.created + self.deadline > datetime.datetime.now()


class Student:
    """Create Student objects."""

    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(home_work: Homework) -> Any:
        """Checks is the deadline of the given homework expired or not.

        Return Homework class object if deadline hasn't expired yet, overwise prints "You are late" and returns None.
        """
        if home_work.is_active():
            return home_work
        print("You are late")
        return None


class Teacher:
    """Create Teacher objects."""

    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(task: str, days_to_do_task: int) -> Homework:
        """Creates an instance of the Homework class object.

        Return Homework class object.
        """
        return Homework(task, days_to_do_task)


if __name__ == "__main__":
    teacher = Teacher("Daniil", "Shadrin")
    student = Student("Roman", "Petrov")
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'
    expired_homework.is_active()  # False

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
