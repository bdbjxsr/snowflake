#coding:utf-8
#说明：    定义了认证相关方法
#作者：    万良卿
#时间：    20171114
from django.shortcuts import render

from framework.decorator import login_required
from framework import auth
from framework.models.auth_model import User

@login_required()
def index(request):
    return render(request, "framework/index.html", {})

def login(request):
    user = User(employee_id='123456', username='hello', password='123')
    auth.login(request, user)
    return render(request, "framework/login.html", {})

def loginPage(request):
    return render(request, "framework/login_page.html", {})

def logout(request):
    auth.logout(request)
    return render(request, "framework/logout.html", {})

def permissionDenied(request):
    return render(request, "framework/permission_denied.html", {})