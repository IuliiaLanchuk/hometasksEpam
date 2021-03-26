import datetime

from task_1_oop.task1_oop import Homework, Student, Teacher


def test_homework_class_attributes():
    homework = Homework("oop", 5)
    assert homework.text == "oop"
    assert homework.deadline == datetime.timedelta(5)


def test_student_class_attributes():
    student = Student("Ivan", "Petrov")
    assert student.last_name == "Ivan"
    assert student.first_name == "Petrov"


def test_teacher_class_attributes():
    teacher = Teacher("Petr", "Ivanov")
    assert teacher.last_name == "Petr"
    assert teacher.first_name == "Ivanov"


def test_homework_is_active_positive():
    homework = Homework("oop", 5)
    assert homework.is_active() is True


def test_homework_is_active_negative():
    homework = Homework("Tasks", 0)
    assert homework.is_active() is False


def test_do_homework_when_homework_is_active_return_homework_class_object():
    student = Student("Ivan", "Ivanov")
    homework = Homework("oop", 5)

    assert student.do_homework(homework) is homework


def test_teacher_create_homework_positive():
    teacher = Teacher("Olga", "Petrovna")
    homework = teacher.create_homework("Generator", 3)

    assert homework.text == "Generator"
    assert homework.deadline == datetime.timedelta(3)
    assert isinstance(homework, Homework) is True


def test_do_homework_when_deadline_is_finished_return_you_are_late(capsys):
    actual_result = Teacher.create_homework("New homework", 0)
    Student.do_homework(actual_result)

    assert "You are late" in capsys.readouterr().out
