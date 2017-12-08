#coding:utf-8
#说明：    基础数据模型用于模型，实现软删除
#作者：    万良卿
#时间：    20171114
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator

from framework.decorator import login_required, permission_required
from framework import auth
from framework.models.auth_model import UserModel, PermissionModel
from framework.models.menu_model import MenuItemModel



class ManageMenuPageView(View):
    def get(self, request, *args, **kwargs):
        menuItems = MenuItemModel.objects.all()
        return render(request, "framework/page_manage.html", {'menuItems':menuItems}) 

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