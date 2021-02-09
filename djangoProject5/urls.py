"""djangoProject5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 学生登陆
    path('studentLogin/', views.studentLogin),
    # 教师登陆
    path('teacherLogin/', views.teacherLogin),
    # 默认访问首页
    path('', views.index),
    path('toIndex/', views.toIndex),
    path('showGrade/', views.showGrade),
    path('queryStudent/', views.queryStudent),
    path('startExam/', views.startExam),
    path('calGrade/', views.calGrade),
    path('logout/', views.logOut),
]
