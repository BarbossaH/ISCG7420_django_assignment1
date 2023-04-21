from django.contrib import admin

# Register your models here.

from .models import GradeBookClass, GradeBooKCourse, Student

admin.site.register(GradeBookClass)
admin.site.register(GradeBooKCourse)
admin.site.register(Student)
