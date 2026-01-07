from django.urls import path
from .views import test_api
from .views import student_list_create, student_details

urlpatterns = [
     path('test/', test_api),
    path("students/",student_list_create),
    path("students/<int:pk>/",student_details),
]