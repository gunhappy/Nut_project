from django.conf.urls import url

from . import views

app_name = 'student_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^table',views.table,name='table'),
    url(r'^insert/$',views.insert,name='insert'),
    url(r'^delete/$',views.delete,name='delete'),
    url(r'^update/$',views.update,name='update'),
]
