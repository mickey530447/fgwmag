from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils.text import slugify
from datetime import date


# Create your models here.

class Role(models.Model):
    role_name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.role_name


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)

    def __str__(self):
        return self.faculty_name


class User(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    avatar_path = models.TextField(null=True)
    birthday = models.DateField()
    sex_boolean = models.BooleanField(null=True)

    def __str__(self):
        return self.username


class FileType(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    filetype = models.ForeignKey(FileType, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=100)
    note = models.TextField()
    contribution_path = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField()
    check_selected = models.BooleanField(default=False)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.title
