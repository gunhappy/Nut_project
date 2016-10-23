from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student

# Create your views here.
def index(request) :
    return render(request,'index.html')

def table(request) :
    student_list = Student.objects.all()
    try :
        student = Student.objects.get(id=request.session['student_id_update'])
        del request.session['student_id_update']
    except KeyError :
        student = None
    return render(request,'tabledata.html',{'student_list':student_list,'update_student':student})

def insert(request) :
    student_id = request.POST['student_id']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    date_regis = request.POST['date_regis']
    section = request.POST['section']
    subject = request.POST['subject']
    teacher = request.POST['teacher']
    attendance_point = request.POST['attendance_point']
    collect_point = request.POST['collect_point']
    test_point = request.POST['test_point']
    student = Student.objects.create(student_id=student_id,firstname=firstname,lastname=lastname,date_regis=date_regis,section=section,subject=subject,teacher=teacher,attendance_point=attendance_point,collect_point=collect_point,test_point=test_point)
    student.save()
    return HttpResponseRedirect(reverse('student_app:index'))

def delete(request) :
    id = request.POST['id']
    student = Student.objects.get(id=id)
    Student.delete(student)
    return HttpResponseRedirect(reverse('student_app:table'))

def update(request) :
    try :
        student = Student.objects.get(id=request.POST['student_id_update'])
        student.student_id = request.POST['student_id']
        student.firstname = request.POST['firstname']
        student.lastname = request.POST['lastname']
        student.date_regis = request.POST['date_regis']
        student.section = request.POST['section']
        student.subject = request.POST['subject']
        student.teacher = request.POST['teacher']
        student.attendance_point = request.POST['attendance_point']
        student.collect_point = request.POST['collect_point']
        student.test_point = request.POST['test_point']
        student.save()
    except KeyError :
        request.session['student_id_update'] = request.POST['student_id_update']
    return HttpResponseRedirect(reverse('student_app:table'))
