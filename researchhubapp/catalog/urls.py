from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispIndex, name='index'),
    path('/home', views.dispHome, name='home'),
    path('student', views.dispStudent, name='student'),
    path('professor', views.dispProfessor, name='professor'),
    path('recruitment', views.dispRecruitment, name='recruitment'),
    path('student/insert', views.studentInsert, name='studentInsert'),
    path('professor/insert', views.professorInsert, name='professorInsert'),
    path('student/update', views.studentUpdate, name='studentUpdate'),
    path('professor/update', views.professorUpdate, name='professorUpdate'),
    path('student/delete', views.studentDelete, name='studentDelete'),
    path('professor/delete', views.professorDelete, name='professorDelete'),
    path('student/studentRecords', views.showStudentDetails, name='showStudentDetails'),
    path('professor/professorRecords', views.showProfessorDetails, name='showProfessorDetails'),
]
