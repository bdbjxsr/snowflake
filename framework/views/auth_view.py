#coding:utf-8
#说明：    定义了认证相关方法
#作者：    万良卿
#时间：    20171114
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator

from framework.decorator import login_required, permission_required
from framework import auth
from framework.models.auth_model import UserModel
from framework.models.menu_model import MenuItemModel

class IndexView(View):    
    def get(self, request, *args, **kwargs):
        mi = MenuItemModel.objects.get_menu(request)    
        return render(request, "framework/index1.html", {'username':request.user.username, 'menu':mi})
    
    @method_decorator(login_required())
    @method_decorator(permission_required(perm=('can_program','can_manage')))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "framework/login.html")
    
    def post(self, request, *args, **kwargs):
        error = ''
        data = request.POST
        employee_id = data.get('employee_id')
        password = data.get('password')
        user= auth.authenticate(employee_id=employee_id, password=password)
        if user :
            auth.login(request, user)
            return HttpResponseRedirect(reverse('framework:index'))
        else:
            employee_id = employee_id
            password = ''
            error = True
            return render(request, 'framework/login.html', {'employee_id':employee_id,'error':error})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return render(request, "framework/logout.html", {})
    
class DenyPermissionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "framework/permission_denied.html", {})