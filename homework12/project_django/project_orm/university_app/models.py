from django.db import models
from django.utils import timezone


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Student(Person):
    group_number = models.IntegerField(default=0)

    def __str__(self):
        return "Student: {} {} group {}".format(
            self.first_name, self.last_name, self.group_number
        )


class Teacher(Person):
    degree = models.CharField(max_length=30, default="professor")

    def __str__(self):
        return "Teacher: {} {}".format(self.first_name, self.last_name)


class Homework(models.Model):
    text = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    created = models.DateTimeField(default=timezone.now)
    teacher_create_hw = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.teacher_create_hw)


class HomeworkResult(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.CharField(max_length=150)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}, {}, {}".format(self.author, self.created, self.homework)
