#coding:utf-8
#说明：    测试view类，用于测试后端方法
#作者：    万良卿
#时间：    20171122
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

class IndexView(View):
    def get(self, request, *args, **kwargs):
        def file_iterator(file_name, chunk_size=512):
            with open(file_name) as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
                    

        file_name = util.creat_temp_file(datetime.now().strftime('%a, %b %d %H:%M'))
        
        response = StreamingHttpResponse(file_iterator(file_name))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
     
        return response
    
    
class ManageView(View):
    def get(self, request, *args, **kwargs):
        FundItems = FundModel.objects.exclude(is_deleted=True)
        ManagerItems = ManagerModel.objects.all()
        return render(request, "stationconfig.html", {'funds':FundItems, 'managers':ManagerItems}) 
    
 
class SelectManager(View):
    def post(self, request, *args, **kwargs):
        manager_id = request.POST['manager_id']
        manager = ManagerModel.objects.get(id=manager_id)
        data = {'manager_code':manager.code}
        data = json.dumps(data)
        print(type(data))
        return HttpResponse(data,content_type="application/json")
  
class QueryJsonManagerView(View):
    def get(self, request, *args, **kwargs):
        managers = ManagerModel.objects.all()
        data = []
        for manager in managers:  
            data.append({'name':manager.name, 'value':manager.id, 'text':manager.name, 'code':manager.code})
            
        
        return JsonResponse({"success":True,"results":data})  
          
class QueryJsonFundView(View):
    def get(self, request, manager, *args, **kwargs):
        if not manager or manager =='':
            funds = FundModel.objects.exclude(is_deleted=True)
            data = []
            for fund in funds:
                data.append({'name':fund.fundname, 'value':fund.fundname, 'text':fund.fundname})
            return JsonResponse({"success":True,"results":data})
        
        if manager and manager !='':
            manager_id = manager
            manager = ManagerModel.objects.get(id=manager_id)
            funds = FundModel.objects.filter(manager=manager)
            data=[]
            for fund in funds:
                data.append({'name':fund.fundname, 'value':fund.fundname, 'text':fund.fundname})
            return JsonResponse({"success":True,"results":data})            
    
    
class SearchFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manage'))
    def post(self, request, *args, **kwargs):
        data = request.POST
        manager_id = data.get('search_manager')
        fund_id = data.get('search_fund')
        fundtype = data.get('search_fundtype')
        history = data.get('search_history')
        ManagerItems = ManagerModel.objects.all()
        FundItems = FundModel.objects.exclude(is_deleted=True)
        if (manager_id !='' and manager_id !=None) or (fund_id !='' and fund_id !=None) or (fundtype !='' and fundtype !=None) or (history !='' and history!= None):
            FundItems1 = FundModel.objects.exclude(is_deleted=True)
            FundItems2 = FundModel.objects.exclude(is_deleted=True)
            FundItems3 = FundModel.objects.exclude(is_deleted=True)
            FundItems4 = FundModel.objects.exclude(is_deleted=True)
            if manager_id !='' and manager_id !=None:
                FundItems1 = FundModel.objects.filter(manager_id=manager_id)
            if fund_id !='' and fund_id !=None:
                FundItems2 = FundModel.objects.filter(id=fund_id)
            if fundtype !='' and fundtype != None:
                FundItems3 = FundModel.objects.filter(type=fundtype)
            if history !='' and history != None:
                FundItems4 = FundModel.objects.filter(is_history=history)
            FundItems = FundItems1 & FundItems2 & FundItems3 & FundItems4
        return render(request, "stationconfig.html", {'funds':FundItems, 'managers':ManagerItems})

class AddFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manage'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        manager_code = data.get('add_manager_code')
        manager = data.get('add_manager')
        fundname = data.get('add_fundname')
        pathfrom = data.get('add_pathfrom')
        pathto_temp = data.get('add_pathto_temp')
        move = data.get('add_move')
        pathto = data.get('add_pathto')
        md = data.get('add_md')
        mput = data.get('add_mput')
        send = data.get('add_send')
        if_exist = data.get('add_if_exist')
        move_file = data.get('add_move_file')
        fund = FundModel.objects.create(manager_code=manager_code, manager=manager, fundname=fundname, pathfrom=pathfrom, pathto_temp=pathto_temp,
                                        move=move, pathto=pathto, md=md, mput=mput, send=send, if_exist=if_exist, move_file=move_file)
        fund.save()
        FundItems = FundModel.objects.exclude(is_deleted=True)
        return render(request, "stationconfig.html", {'funds':FundItems}) 
    
    
class ModifyFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manage'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        fundid = data.get('modify_fundid')
        manager_code = data.get('modify_manager_code')
        manager = data.get('modify_manager')
        fundname = data.get('modify_fund')
        fundcode = data.get('modify_fundcode')
        fundtype = data.get('modify_fundtype')
        history = data.get('modify_history')
        
        pathfrom = data.get('modify_pathfrom')
        pathto_temp = data.get('modify_pathto_temp')
        move = data.get('modify_move')
        pathto = data.get('modify_pathto')
        md = data.get('modify_md')
        mput = data.get('modify_mput')
        send = data.get('modify_send')
        if_exist = data.get('modify_if_exist')
        move_file = data.get('modify_move_file')   
        FundModel.objects.filter(id=fundid).update(fundname=fundname, code=fundcode, type=fundtype, is_history=history, pathfrom=pathfrom, pathto_temp=pathto_temp,
                                        move=move, pathto=pathto, md=md, mput=mput, send=send, if_exist=if_exist, move_file=move_file)
        fund = FundModel.objects.get(id=fundid)
        manager = ManagerModel.objects.get(id=manager)
        fund.manager = manager
        fund.save()
        FundItems = FundModel.objects.exclude(is_deleted=True)
        return render(request, "stationconfig.html", {'funds':FundItems})
    
class DeleteFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:manage'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        fundid = data.get('delete_fundid')
        FundModel.objects.filter(id=fundid).update(is_deleted=True)
        FundItems = FundModel.objects.exclude(is_deleted=True)
        return render(request, "stationconfig.html", {'funds':FundItems})
    
class ExportGetFile(View):
    def get(self, request, *args, **kwargs):
        header = 'set mydate=%date:~0,4%%date:~5,2%%date:~8,2%'+'\r\n'+'set pathfrom=E:\\\\recv\\\\'+'\r\n'+'set pathto=E:\\XBRL\\xbrl\\'+'\r\n'
        getfile = ''
        for fund in FundModel.objects.exclude(is_deleted=True):
            getfile = getfile+'java -Dfile.encoding=GBK  -cp E:\\\\lgfilecomm-1.4.2.6.jar com.filecomm.fileClient mget 10.99.165.82 8686 10.99.165.82 %pathfrom%'\
                      +fund.pathfrom+' % pathto%'+fund.pathto_temp+'\r\n'+'move %pathto%'+fund.move+' %pathto%'+fund.pathto+'\r\n' \
                      +'del  %pathto%'+fund.pathto_temp+'* /Q'+'\r\n\r\n'
        response = HttpResponse(header+getfile)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format("GetFile.bat")
        return response
    
class ExportPutFile(View):
    def get(self, request, *args, **kwargs):
        header = 'set mydate=%date:~0,4%%date:~5,2%%date:~8,2%'+'\r\n'
        putfile = ''
        for fund in FundModel.objects.exclude(is_deleted=True):
            putfile = putfile+'md E:\\XBRL\\sign\\'+fund.md+'send\r\n'+'copy /y E:\\XBRL\\sign\\'+fund.md+'CN* E:\\XBRL\\sign\\'+fund.md+'send\\'+'\r\n'\
                      +'java -Dfile.encoding=GBK  -cp E:\\\\lgfilecomm-1.4.2.6.jar com.filecomm.fileClient mput 10.99.165.82 8686 10.99.165.82 E:/XBRL/sign/'\
                      +fund.mput+'send/ E:/send/'+fund.send+'\r\n'+'rd /s/q E:\\XBRL\\sign\\'+fund.md+'send\r\n\r\n'
        response = HttpResponse(header+putfile)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format("PutFile.bat")
        return response
    
class ExportMoveFile(View):
    def get(self, request, *args, **kwargs):
        movefile = ''
        for fund in FundModel.objects.exclude(is_deleted=True):
            movefile = movefile+'IF EXIST E:\\XBRL\\sign\\'+fund.if_exist+' move E:\\XBRL\\sign\\'+fund.if_exist\
                       +'  E:\\XBRL\\sign\\'+fund.move_file+'\r\n'
        response = HttpResponse(movefile)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format("MoveFile.bat")
        return response