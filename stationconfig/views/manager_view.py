#coding:utf-8
#说明：    管理人View
#作者：    阙泠伊
#时间：    20180130
import json
from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse, StreamingHttpResponse, JsonResponse
from django.core import serializers
from django.core.urlresolvers import reverse
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render, render, get_object_or_404, redirect
from django.db.models import Q

from stationconfig import util
from stationconfig.models.models import TemplateModel, FundModel, ManagerModel
from stationconfig.forms.forms import SelectManager
from os import name

class ManagerView(View):
    def get(self, request, *args, **kwargs):
        ManagerItems = ManagerModel.objects.exclude(is_deleted=True)
        return render(request, "Manager.html", {'managers':ManagerItems})

class QueryJsonManagerCodeView(View):
    def get(self, request, *args, **kwargs):
        managers = ManagerModel.objects.all().order_by('code')
        data = []
        for manager in managers:  
            data.append({'name':manager.code, 'value':manager.code, 'text':manager.code})
            
        return JsonResponse({"success":True,"results":data}) 
    
class SearchManagerView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manager'))
    def post(self, request, *args, **kwargs):
        data = request.POST
        manager_id = data.get('search_manager')
        manager_code = data.get('search_manager_code')
        fundname = data.get('search_fund')
        ManagerItems = ManagerModel.objects.exclude(is_deleted=True)
        FundItems = FundModel.objects.exclude(is_deleted=True)
        if manager_id !='' and manager_id !=None:
            ManagerItems = ManagerModel.objects.filter(id=manager_id)
        if manager_code !='' and manager_code !=None:
            ManagerItems = ManagerModel.objects.filter(code=manager_code)
        if fundname !='' and fundname !=None:
            ManagerItems = []
            FundItem = FundModel.objects.get(fundname=fundname)
            for manager in ManagerModel.objects.exclude(is_deleted=True):
                for fund in manager.test.all():
                    if fund.fundname==FundItem.fundname:
                        ManagerItems.append(manager)
        print('aa')
        return render(request, "Manager.html", {'managers':ManagerItems})

class AddManagerView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manager'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        name = data.get('add_manager')
        code = data.get('add_manager_code')
        if name!='' and code!='':
            manager = ManagerModel.objects.create(name=name, code=code)
        ManagerItems = ManagerModel.objects.exclude(is_deleted=True).order_by('code')
        return render(request, "Manager.html", {'managers':ManagerItems}) 
    
    
class ModifyManagerView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manager'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        manager_id = data.get('modify_manager_id')
        name = data.get('modify_manager')
        code = data.get('modify_manager_code')
        if name!='' and code!='':
            ManagerModel.objects.filter(id=manager_id).update(name=name, code=code)
        ManagerItems = ManagerModel.objects.exclude(is_deleted=True).order_by('code')
        return render(request, "Manager.html", {'managers':ManagerItems}) 
    
    
class DeleteManagerView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manager'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        manager_id = data.get('delete_manager_id')
        print("a+"+manager_id)
        ManagerModel.objects.filter(id=manager_id).update(is_deleted=True)
        ManagerItems = ManagerModel.objects.exclude(is_deleted=True).order_by('code')
        return render(request, "Manager.html", {'managers':ManagerItems})