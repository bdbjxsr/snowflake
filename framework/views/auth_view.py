#coding:utf-8
#说明：    定义了认证相关方法
#作者：    万良卿
#时间：    20171114
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render

from framework.decorator import login_required
from framework import auth
from framework.models.auth_model import User
from test.test_typing import Employee

@login_required()
def index(request):
    return render(request, "framework/index.html", {})


def login(request):
    if request.method =='POST':
        data = request.POST
        employee_id = data.get('employee_id')
        password = data.get('password')
        user= auth.authenticate(employee_id=employee_id, password=password)
        if user :
            auth.login(request, employee_id)
            return HttpResponseRedirect(reverse('framework:index'))
        else:
            employee_id = employee_id
            password=''
            return render(request, 'framework/login.html', {'employee_id':employee_id,'user':user})
    return render(request, "framework/login.html", {'user':True})



def logout(request):
    auth.logout(request)
    return render(request, "framework/logout.html", {})

def permissionDenied(request):
    return render(request, "framework/permission_denied.html", {})