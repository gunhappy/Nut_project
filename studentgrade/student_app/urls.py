from django.conf.urls import url

from . import views

app_name = 'student_app'

urlpatterns = [
    url(r'^$',views.loginForm,name='loginForm'),
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$',views.regisForm,name='regisForm'),
    url(r'^regis/$',views.register,name='register'),
    url(r'^table',views.table,name='table'),
    url(r'^insert/$',views.insert,name='insert'),
    url(r'^delete/$',views.delete,name='delete'),
    url(r'^update/$',views.update,name='update'),
]
