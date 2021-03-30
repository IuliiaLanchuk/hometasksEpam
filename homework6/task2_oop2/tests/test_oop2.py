import datetime

import pytest
from project2_oop2.oop2 import (
    DeadlineError,
    Homework,
    HomeworkResult,
    HomeworkTypeError,
    Student,
    Teacher,
)


def test_teacher_class_attributes():
    opp_teacher = Teacher("Daniil", "Shadrin")

    assert opp_teacher.first_name == "Daniil"
    assert opp_teacher.last_name == "Shadrin"


def test_student_class_attributes():
    lazy_student = Student("Roman", "Petrov")

    assert lazy_student.first_name == "Roman"
    assert lazy_student.last_name == "Petrov"


def test_teacher_create_homework():
    opp_teacher = Teacher("Daniil", "Shadrin")
    oop_hw = opp_teacher.create_homework("Learn OOP", 1)

    assert oop_hw.text == "Learn OOP"
    assert oop_hw.deadline == datetime.timedelta(days=1)


def test_active_homework_is_done_by_student():
    good_student = Student("Lev", "Sokolov")
    active_hw = Homework("Learn OOP", 2)
    result_of_active_hw = good_student.do_homework(
        active_hw, "result of active homework"
    )

    assert isinstance(result_of_active_hw, HomeworkResult)
    assert result_of_active_hw.solution == "result of active homework"
    assert result_of_active_hw.homework.text == "Learn OOP"


def test_inactive_homework_raise_deadline_error():
    lazy_student = Student("Roman", "Petrov")
    hw_inactive = Homework("Read docs", 0)
    with pytest.raises(DeadlineError, match="You are late"):
        lazy_student.do_homework(hw_inactive, "result of inactive homework")


def test_homework_result_constructor_raises_an_error_on_wrong_argument_type():
    with pytest.raises(HomeworkTypeError, match="You gave not a Homework object"):
        assert HomeworkResult(
            Student("Roman", "Petrov"), "it is not a Homework class object", "Solution"
        ).homework


def test_teacher_check_homework_with_length_more_than_5_result_in_add_in_homework_done_data_structure():
    good_student = Student("Lev", "Sokolov")
    opp_teacher = Teacher("Daniil", "Shadrin")
    oop_hw = opp_teacher.create_homework("Learn OOP", 2)
    result_positive = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result_positive)

    assert "Learn OOP" in opp_teacher.homework_done
    assert "Learn OOP" in Teacher.homework_done
    assert (
        "I have done this hw"
        in opp_teacher.homework_done[result_positive.homework.text]
    )


def test_teacher_check_homework_with_length_less_than_5_result_in_not_add_in_homework_done_data_structure():
    bad_student = Student("Ivan", "Sokolovskiy")
    opp_teacher = Teacher("Daniil", "Shadrin")
    hw_task = opp_teacher.create_homework("Learn english", 2)
    result_negative = bad_student.do_homework(hw_task, "< 5")
    opp_teacher.check_homework(result_negative)

    assert "Learn english" not in opp_teacher.homework_done
    assert "< 5" not in opp_teacher.homework_done[result_negative.homework.text]


def test_reset_homework_deletes_only_given_homework():
    teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")
    lazy_student = Student("Ivan", "Ivanov")
    homework1 = teacher.create_homework("Learn OOP", 1)
    homework2 = teacher.create_homework("Create Class Homework", 2)
    result_hw1 = good_student.do_homework(homework1, "Lev Sokolov has done this hw")
    result_hw2 = lazy_student.do_homework(homework2, "Ivan Ivanov has done this hw")
    teacher.check_homework(result_hw1)
    teacher.check_homework(result_hw2)

    assert Teacher.homework_done[homework1.text]
    assert Teacher.homework_done[homework2.text]
    Teacher.reset_results(homework1)
    assert not Teacher.homework_done[homework1.text]
    assert Teacher.homework_done[homework2.text]


def test_reset_homework_was_not_given_as_an_argument_result_in_full_reset():
    teacher = Teacher("Daniil", "Shadrin")
    good_student = Student("Lev", "Sokolov")
    lazy_student = Student("Ivan", "Ivanov")
    homework1 = teacher.create_homework("Learn OOP", 1)
    homework2 = teacher.create_homework("Create Class Homework", 2)
    result_hw1 = good_student.do_homework(homework1, "Lev Sokolov has done this hw")
    result_hw2 = lazy_student.do_homework(homework2, "Ivan Ivanov has done this hw")
    teacher.check_homework(result_hw1)
    teacher.check_homework(result_hw2)

    assert Teacher.homework_done[homework1.text]
    assert Teacher.homework_done[homework2.text]
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0
