from django.contrib import admin

from .models import Homework, HomeworkResult, Person, Student, Teacher


class HomeworkAdmin(admin.ModelAdmin):
    pass


class PersonAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


class HomeworkResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(HomeworkResult, HomeworkResultAdmin)
