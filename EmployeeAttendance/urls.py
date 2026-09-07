from django.urls import path
from django.shortcuts import redirect

from . import views

def redirect_to_index(request):
    return redirect('index')

urlpatterns = [path("", redirect_to_index, name="home"),
			path("index.html", views.index, name="index"),
			path("UserLogin.html", views.UserLogin, name="UserLogin"),
			path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
			path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),
			path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
			path("AddEmp.html", views.AddEmp, name="AddEmp"),
			path("AddEmpAction", views.AddEmpAction, name="AddEmpAction"),
			path("ViewEmp", views.ViewEmp, name="ViewEmp"),
			path("ViewEmpAttendance", views.ViewEmpAttendance, name="ViewEmpAttendance"),
			path("ViewEmpAttendanceAction", views.ViewEmpAttendanceAction, name="ViewEmpAttendanceAction"),
			path("ViewAttendance", views.ViewAttendance, name="ViewAttendance"),
			path("ViewAttendanceAction", views.ViewAttendanceAction, name="ViewAttendanceAction"),
			path("DownloadAction", views.DownloadAction, name="DownloadAction"),
			path("test.html", views.test, name="test"),
]
