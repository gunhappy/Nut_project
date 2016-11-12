from django.conf.urls import url

from . import views

app_name = 'student_app'

urlpatterns = [
    url(r'^$',views.loginForm,name='loginForm'),
    url(r'^attendance/$',views.attendaceForm,name='attendaceForm'),
    url(r'^scores/$',views.scoresForm,name='scoresForm'),
    url(r'^findStudent/$',views.findStudent,name='findStudent'),
    url(r'^findStudentAttendance/$',views.findStudentAttendance,name='findStudentAttendance'),
    url(r'^findStudentScores/$',views.findStudentScores,name='findStudentScores'),
    url(r'^updateAttendance/$',views.updateAttendance,name='updateAttendance'),
    url(r'^updateScores/$',views.updateScores,name='updateScores'),
    url(r'^updateStudent/$',views.updateStudent,name='updateStudent'),
    url(r'^addstudent/$',views.addstudent,name='addstudent'),
    url(r'^student/$',views.studentForm,name='studentForm'),
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^register/$',views.regisForm,name='regisForm'),
    url(r'^regis/$',views.register,name='register'),
    url(r'^table',views.table,name='table'),
    url(r'^insert/$',views.insert,name='insert'),
    url(r'^delete/$',views.delete,name='delete'),
]
