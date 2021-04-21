from django.db import models


class Homework(models.Model):
    text = models.TextField()
    deadline = models.DateTimeField()
    created = models.DateTimeField()


class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)


class Student(Person):
    ...


class Teacher(Person):
    ...


class HomeworkResult(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    solution = models.TextField()
    created = models.DateTimeField()
