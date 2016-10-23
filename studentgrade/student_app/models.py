from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=11)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_regis = models.DateField()
    section = models.CharField(max_length=5)
    subject = models.CharField(max_length=50)
    teacher = models.CharField(max_length=100)
    attendance_point = models.IntegerField()
    collect_point = models.IntegerField()
    test_point = models.IntegerField()
