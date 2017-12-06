#coding:utf-8
#说明：    基础数据模型用于模型，实现软删除
#作者：    万良卿
#时间：    20171114
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render

from framework.decorator import login_required, permission_required
from framework import auth
from framework.models.auth_model import User
from framework.models.menu_model import MenuItem

def pageManageView(request):
    menuItems = MenuItem.objects.all()
    return render(request, "framework/page_manage.html", {'menuItems':menuItems}) 