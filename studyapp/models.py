from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# A sample
# every single attribute represent a column inside of the database
# class Project(models.Model):
#     title = models.CharField()
#     description = models.TextField()
#     id = models.UUIDField()


class GradeBookClass(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # if topic is deleted, the room should be kept, so topic also can be empty, that's why we must setup null=true
    topic = models.ForeignKey("GradeBooKCourse", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    # default value is false, which means cannot have a blank.
    # blank = true means when adding a form, it can be blank
    description = models.TextField(null=True, blank=True)
    # participants=

    # add the date of created and update
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # the newest post will be at the top, using updated first, if the updated is same, then using created
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # one to many, CASCADE= when parent deleted, children will be deleted simultaneously
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class GradeBooKCourse(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
