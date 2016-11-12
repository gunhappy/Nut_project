from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
import django.contrib.auth  as auth
from .models import Student,Attendance,Scores

# Create your views here.
def index(request) :
    return render(request,'index.html')

def addstudent(request) :
    return render(request,'addstudent.html')

def studentForm(request) :
    return render(request,'student.html',{'student_edit':False})

def attendaceForm(request):
    return render(request,'attendance.html',{'attendance_edit':False})

def scoresForm(request):
    return render(request,'scores.html',{'scores_edit':False})

def loginForm(request) :
    return render(request,'login.html')

def regisForm(request) :
    return render(request,'register.html')

def register(request) :
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username,email,password)
    user.save()
    return HttpResponseRedirect(reverse('student_app:loginForm'))

def login(request) :
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None :
        auth.login(request,user)
        return HttpResponseRedirect(reverse('student_app:index'))
    else :
        return HttpResponseRedirect(reverse('student_app:loginForm'))

def logout(request) :
    return render(request,'login.html')

def table(request) :
    teacher = request.user
    student_list = Student.objects.all().filter(teacher_id=teacher.id)
    students = []
    for student in student_list:
        scores =  Scores.objects.get(student_id=student.id)
        students.append({'student':student,'scores':scores})

    return render(request,'tabledata.html',{'student_list':students})

def insert(request) :
    user = request.user
    teacher_id = user
    student_id = request.POST['student_id']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    id_number = request.POST['id_number']
    birthday = request.POST['birthday']
    address = request.POST['address']
    telephone = request.POST['telephone']
    teacher_subject = request.POST['teacher_subject']
    main_subject =  request.POST['main_subject']
    date_regis = request.POST['date_regis']
    section = request.POST['section']
    try:
        student = Student.objects.create(teacher_id=teacher_id,student_id=student_id,firstname=firstname,lastname=lastname,id_number=id_number,birthday=birthday,address=address,telephone=telephone,teacher_subject=teacher_subject,main_subject=main_subject,date_regis=date_regis,section=section)
        student.save()
        attendance = Attendance.objects.create(student_id=student)
        attendance.save()
        scores = Scores.objects.create(student_id=student)
        scores.save()
        return HttpResponseRedirect(reverse('student_app:addstudent'))
    except:
        return HttpResponseRedirect(reverse('student_app:addstudent'))

def findStudent(request):
    student_id = request.POST['student_id']
    teacher = request.user
    try:
        student = Student.objects.get(student_id=student_id,teacher_id=teacher.id)
        return render(request,'student.html',{'student':student})
    except:
        return HttpResponseRedirect(reverse('student_app:studentForm'))

def findStudentAttendance(request):
    student_id = request.POST['student_id']
    teacher = request.user
    try:
        student = Student.objects.get(student_id=student_id,teacher_id=teacher.id)
        attendance =  Attendance.objects.get(student_id=student.id)
        return render(request,'attendance.html',{'attendance':attendance,'student':student})
    except:
        return HttpResponseRedirect(reverse('student_app:attendaceForm'))

def findStudentScores(request):
    student_id = request.POST['student_id']
    teacher = request.user
    try:
        student = Student.objects.get(student_id=student_id,teacher_id=teacher.id)
        scores =  Scores.objects.get(student_id=student.id)
        return render(request,'scores.html',{'scores':scores,'student':student})
    except:
        return HttpResponseRedirect(reverse('student_app:scoresForm'))

def updateAttendance(request):
    student_id = request.POST['id']
    try:
        student = Student.objects.get(student_id=student_id)
        try:
            attendance =  Attendance.objects.get(student_id=student.id)
            attendance.attend_times = request.POST['attend_times']
            attendance.absent_times = request.POST['absent_times']
            attendance.save()
            return render(request,'attendance.html',{'attendance':attendance,'student':student})
        except:
            attendance =  Attendance.objects.get(student_id=student.id)
            return render(request,'attendance.html',{'attendance_edit':True,'student':student,'attendance':attendance})
        return render(request,'attendance.html',{'attendance_edit':True,'student':student})
    except:
        return HttpResponseRedirect(reverse('student_app:attendaceForm'))

def updateStudent(request):
    student_id = request.POST['id']
    try:
        student = Student.objects.get(student_id=student_id)
        try:
            student.student_id = request.POST['student_id']
            student.firstname = request.POST['firstname']
            student.lastname = request.POST['lastname']
            student.id_number = request.POST['id_number']
            student.birthday = request.POST['birthday']
            student.address = request.POST['address']
            student.telephone = request.POST['telephone']
            student.teacher_subject = request.POST['teacher_subject']
            student.main_subject = request.POST['main_subject']
            student.date_regis = request.POST['date_regis']
            student.section = request.POST['section']
            student.save()
            return render(request,'student.html',{'student':student})
        except:
            attendance =  Attendance.objects.get(student_id=student.id)
            return render(request,'student.html',{'student_edit':True,'student':student})
        return render(request,'student.html',{'student_edit':True,'student':student})
    except:
        return HttpResponseRedirect(reverse('student_app:attendaceForm'))

def updateScores(request):
    student_id = request.POST['id']
    try:
        student = Student.objects.get(student_id=student_id)
        try:
            scores =  Scores.objects.get(student_id=student.id)
            scores.attendance_point = request.POST['attendance_point']
            scores.mental_point = request.POST['mental_point']
            scores.collect_point = request.POST['collect_point']
            scores.midterm_point = request.POST['midterm_point']
            scores.final_point = request.POST['final_point']
            scores.save()
            return render(request,'scores.html',{'scores':scores,'student':student})
        except:
            scores =  Scores.objects.get(student_id=student.id)
            return render(request,'scores.html',{'scores_edit':True,'student':student,'scores':scores})
        return render(request,'scores.html',{'scores_edit':True,'student':student})
    except:
        return HttpResponseRedirect(reverse('student_app:scoresForm'))

def delete(request) :
    student_id = request.POST['student_id']
    student = Student.objects.get(student_id=student_id)
    Student.delete(student)
    return HttpResponseRedirect(reverse('student_app:table'))

# def update(request) :
#     try :
#         student = Student.objects.get(id=request.POST['student_id_update'])
#         student.student_id = request.POST['student_id']
#         student.firstname = request.POST['firstname']
#         student.lastname = request.POST['lastname']
#         student.date_regis = request.POST['date_regis']
#         student.section = request.POST['section']
#         student.subject = request.POST['subject']
#         student.teacher = request.POST['teacher']
#         student.attendance_point = request.POST['attendance_point']
#         student.collect_point = request.POST['collect_point']
#         student.test_point = request.POST['test_point']
#         student.save()
#     except KeyError :
#         request.session['student_id_update'] = request.POST['student_id_update']
#     return HttpResponseRedirect(reverse('student_app:table'))
