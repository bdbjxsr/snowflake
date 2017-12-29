#coding:utf-8
#说明：    基础数据模型用于模型，实现软删除
#作者：    万良卿
#时间：    20171114
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django import forms
from django.db.models import Q

from framework.decorator import login_required, permission_required
from framework import auth
from framework.models.auth_model import UserModel, PermissionModel, DepartmentModel
from framework.models.menu_model import MenuItemModel



class ManageMenuPageView(View):
    def get(self, request, *args, **kwargs):
        menuItems = MenuItemModel.objects.all()
        return render(request, "framework/page/page_manage.html", {'menuItems':menuItems}) 

class AddMenuPageView(View):
    def post(self, request, *args, **kwargs):
        data = request.POST
        name = data.get('name')
        code = data.get('code')
        url = data.get('url')        
        sort_seq = data.get('sort_seq')
        icon = data.get('icon')
        permission = data.get('permission')        
        mi2 = MenuItemModel.objects.create(name=name, code=code, icon =icon, sort_seq=sort_seq, url=url, permission_id=permission)
            
        return HttpResponse("excute success")

class QueryJsonPermissionView(View):
    def get(self, request, *args, **kwargs):
        permissions = PermissionModel.objects.all()
        data = []
        for permission in permissions:  
            data.append({'name':permission.name, 'value':permission.id})
            
        return JsonResponse({"success":True,"results":data})
    
    
class ManageUserView(View):
    def get(self, request, *args, **kwargs):
        userItems = UserModel.objects.all()
        superiors = [] 
        for user in UserModel.objects.all():
            if not user.superiors:
                superiors.append(user) 
        return render(request, "framework/page/user_manage.html", {'user':userItems, 'superiors':superiors}) 


class SearchUserView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('framework:user_manage'))
        
    def post(self, request, *args, **kwargs):
        data = request.POST
        employee_id = data.get('find_employee_id')
        username = data.get('find_username')
        dprt_id = data.get('find_dprt')
        sp_dprt_id = data.get('find_spdprt')
        superior = data.get('find_superior')
        
        userItems = UserModel.objects.all()
        if employee_id !='' or username !='' or (dprt_id !='' and dprt_id !='none') or (sp_dprt_id !='' and sp_dprt_id !='none'):
            userItems1 = UserModel.objects.all()
            userItems2 = UserModel.objects.all()
            userItems3 = UserModel.objects.all()
            userItems4 = UserModel.objects.all()
            if employee_id !='':
                userItems1 = UserModel.objects.filter(Q(employee_id__icontains=employee_id))
            if username !='':
                userItems2 = UserModel.objects.filter(Q(username__icontains=username))
            if dprt_id !='' and dprt_id !='none':
                userItems3 = UserModel.objects.filter(department_id=dprt_id)
            if sp_dprt_id !='' and sp_dprt_id !='none':
                if dprt_id !='' and dprt_id !='none':
                    userItems4 = userItems3
                else:
                    dprtItems = DepartmentModel.objects.filter(super_department_id=sp_dprt_id)
                    userItems4 = UserModel.objects.filter(department_id=dprtItems[0].id)
                    for dprt in dprtItems:
                        users = UserModel.objects.filter(department_id=dprt.id)     
                        userItems4 = userItems4 | users
            userItems = userItems1 & userItems2 & userItems3 & userItems4
       
        return render(request, "framework/page/user_manage.html", {'user':userItems, 
                                                                   'find_employee_id':employee_id, 'find_username':username,
                                                                   'find_dprt':dprt_id,'find_spdprt':sp_dprt_id, })
        
class QueryJsonDepartmentView(View):
    def get(self, request, *args, **kwargs):
        data = []
        for dp_temp in DepartmentModel.objects.all():
            if dp_temp.super_department:
                data.append({'name':dp_temp.name, 'value':dp_temp.id}) 
        return JsonResponse({"success":True,"results":data})
    def post(self, request, *args, **kwargs):
        spdprt = request.get('spdprt')
        data= []
        for dp_temp in DepartmentModel.objects.all():
            if dp_temp.super_department.name == spdprt:
                data.append({'name':dp_temp.name, 'value':dp_temp.id})
        return JsonResponse({"success":True,"results":data})


class QueryJsonSuperDepartmentView(View):
    def get(self, request, *args, **kwargs):
        data = []
        for dp_temp in DepartmentModel.objects.all():
            if not dp_temp.super_department:
                data.append({'name':dp_temp.name, 'value':dp_temp.id}) 
        return JsonResponse({"success":True,"results":data})
    

class AddUserView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('framework:user_manage'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        employee_id = data.get('add_employee_id')
        username = data.get('add_username')
        dprt_id = data.get('add_dprt')
        sp_dprt_id = data.get('add_spdprt')
        superior = data.get('add_superiors')   
        user = UserModel.create_user(employee_id=employee_id, username=username, password="00000")
        user.department_id = dprt_id
        if superior !='':
            sp_user = UserModel.objects.get(employee_id=superior)
            user.superior.add(sp_user)
        user.save()
        userItems = UserModel.objects.all()
        return render(request, "framework/page/user_manage.html", {'user':userItems})    
        
class ModifyUserView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('framework:user_manage'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        employee_id = data.get('modify_employee_id')
        username = data.get('modify_username')
        dprt_id = data.get('modify_dprt') 
        print(dprt_id)
        sp_dprt_id = data.get('modify_spdprt')
        superior = data.get('modify_superiors')   
        UserModel.objects.filter(employee_id=employee_id).update(username=username)
        user = UserModel.objects.get(employee_id=employee_id)
        user.department_id = dprt_id
        user.save()
        userItems = UserModel.objects.all()
        return render(request, "framework/page/user_manage.html", {'user':userItems})
    
class DeleteUserView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('framework:user_manage'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        employee_id = data.get('post_id')
        UserModel.objects.filter(employee_id=employee_id).update(is_deleted=True)
        userItems = UserModel.objects.exclude(is_deleted=True)
        return render(request, "framework/page/user_manage.html", {'user':userItems})