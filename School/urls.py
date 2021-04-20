"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [

    path("",views.home,name='home'),
    path("adform",views.adform,name='adform'),
    path('dimm',views.dimm, name='dimm'),

    #office
    path('login',views.login, name='login'),

    #student
    path('student',views.student,name="student"),
    path('slog', views.slog, name="slog"),
    path('stdsignup', views.stdsignup, name="stdsignup"),
    path('adstd', views.adstd,name="adstd"),
    path('sexam', views.sexam, name="sexam"),
    path("liv", views.liv, name="liv"),
    #teacher
    path('teacher',views.teacher,name ="teacher"),
    path('techsineup', views.tecsin, name="tecsin"),
    path('adtech', views.adtech, name="adtech"),
    path('tlog',views.tlog,name='tlog'),
    path('taddstd', views.taddstd, name='taddstd'),

    path('logs', views.logs, name='logs'),
    path('signup', views.signup, name='signup'),
    path('adminadd', views.adminadd, name='adminadd'),
    path("update/<int:id>",views.update,name='update'),
    path("delete/<int:id>",views.delete,name="delete"),
    path("dip",views.display, name="display"),
    path("inq",views.inq, name="inq"),
    path("otp", views.otp, name="otp"),
    path("veri", views.veri,name="veri"),
    path("back", views.back,name="back"),

    path('name',views.search, name ='search'),
    path('id', views.search, name='search'),
    path('std', views.search, name='search'),
    path('search', views.search, name='search'),
    path('slogof', views.slogof, name='slogof'),
    path('logoff', views.logoff, name='logoff'),
    path('tlogof', views.tlogof, name='tlogof'),
    ## Exam
    path('omm', views.exam, name="exam"),
    path('exam2', views.exam2, name="exam2"),
    path('exoffice', views.exoffice, name="exoffice"),


]
