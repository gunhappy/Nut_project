from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    teacher_id = models.ForeignKey(User)
    student_id = models.CharField(max_length=11, default=None)
    firstname = models.CharField(max_length=50, default=None)
    lastname = models.CharField(max_length=50, default=None)
    id_number = models.CharField(max_length=13, default=None)
    birthday = models.DateField(default=None)
    address = models.CharField(max_length=100, default=None)
    telephone = models.CharField(max_length=10, default=None)
    teacher_subject = models.CharField(max_length=50, default=None)
    main_subject =  models.CharField(max_length=50, default=None)
    date_regis = models.DateField(default=None)
    section = models.CharField(max_length=5, default=None)

class Attendance(models.Model):
    student_id = models.ForeignKey(Student)
    attend_times = models.IntegerField(default=0)
    absent_times = models.IntegerField(default=0)

class Scores(models.Model):
    student_id = models.ForeignKey(Student)
    attendance_point = models.IntegerField(default=0)
    mental_point = models.IntegerField(default=0)
    collect_point = models.IntegerField(default=0)
    midterm_point = models.IntegerField(default=0)
    final_point = models.IntegerField(default=0)
