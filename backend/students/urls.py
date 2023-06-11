from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from rest_framework import routers


from . import views

# route=routers.DefaultRouter()
# route.register("",St)

urlpatterns = [
    path("students/", views.studentsInfo,name="All students information"),
    path("students/<str:pk>", views.studentInfo,name="one student information"),
    path("add_student/", views.Addstudent,name="one student add"),
    path("delete_student/<str:pk>", views.delete_student,name="student delete"),
    path("update_student/<str:pk>", views.update_student,name="student update"),
]

