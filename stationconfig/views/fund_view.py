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


class FundView(View):
    def get(self, request, *args, **kwargs):
        FundItems = FundModel.objects.exclude(is_deleted=True).order_by('fundname')
        ManagerItems = ManagerModel.objects.all().order_by('code')
        return render(request, "stationconfig.html", {'funds':FundItems, 'managers':ManagerItems}) 
    
 
class SelectManager(View):
    def post(self, request, *args, **kwargs):
        manager_id = request.POST['manager_id']
        manager = ManagerModel.objects.get(id=manager_id)
        data = {'manager_code':manager.code}
        data = json.dumps(data)
        return HttpResponse(data,content_type="application/json")
  
  
class QueryJsonManagerView(View):
    def get(self, request, *args, **kwargs):
        managers = ManagerModel.objects.exclude(is_deleted=True).order_by('code')
        data = []
        for manager in managers:  
            data.append({'name':manager.name, 'value':manager.id, 'text':manager.name})
            
        return JsonResponse({"success":True,"results":data})  
          
          
class QueryJsonFundView(View):
    def get(self, request, manager, *args, **kwargs):
        if not manager or manager =='':
            funds = FundModel.objects.exclude(is_deleted=True).order_by('fundname')
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
    

class QueryJsonTableData(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"success":True,"results":data}) 

    
class SearchFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:fund'))
    def post(self, request, *args, **kwargs):
        data = request.POST
        manager_id = data.get('search_manager')
        fundname = data.get('search_fund')
        fundtype = data.get('search_fundtype')
        history = data.get('search_history')
        ManagerItems = ManagerModel.objects.all().order_by('code')
        FundItems = FundModel.objects.exclude(is_deleted=True).order_by('fundname')
        if (manager_id !='' and manager_id !=None) or (fundname !='' and fundname !=None) or (fundtype !='' and fundtype !=None) or (history !='' and history!= None):
            FundItems1 = FundModel.objects.exclude(is_deleted=True)
            FundItems2 = FundModel.objects.exclude(is_deleted=True)
            FundItems3 = FundModel.objects.exclude(is_deleted=True)
            FundItems4 = FundModel.objects.exclude(is_deleted=True)
            if manager_id !='' and manager_id !=None:
                FundItems1 = FundModel.objects.filter(manager_id=manager_id).order_by('fundname')
            if fundname !='' and fundname !=None:
                FundItems2 = FundModel.objects.filter(fundname=fundname).order_by('fundname')
            if fundtype !='' and fundtype != None:
                FundItems3 = FundModel.objects.filter(type=fundtype).order_by('fundname')
            if history !='' and history != None:
                FundItems4 = FundModel.objects.filter(is_history=history).order_by('fundname')
            FundItems = FundItems1 & FundItems2 & FundItems3 & FundItems4
        return render(request, "stationconfig.html", {'funds':FundItems, 'managers':ManagerItems})


class AddFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:fund'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        manager_exist = data.get('add_manager_exist')
        manager_code_exist = data.get('add_manager_code_exist')
        manager_new = data.get('add_manager_new')
        manager_code_new = data.get('add_manager_code_new')
        fundname = data.get('add_fundname')
        fundcode = data.get('add_fundcode')
        fundtype = data.get('add_fundtype')
        history = data.get('add_history')
        if manager_exist!='' and manager_new=='':
            manager = ManagerModel.objects.get(id=manager_exist)
        if manager_code_exist=='' and manager_new!='':
            manager = ManagerModel.objects.create(name=manager_new, code=manager_code_new)
        if fundtype =='xbrl':
            if history == 'True':
                pathfrom = data.get('add_pathfrom')
                pathto_temp = data.get('add_pathto_temp')
                move = data.get('add_move')
                pathto = data.get('add_pathto')
                md = data.get('add_md')
                mput = data.get('add_mput')
                send = data.get('add_send')
                if_exist = data.get('add_if_exist')
                move_file = data.get('add_move_file')
                
            if history == 'False':
                pathfrom1 = data.get('add_pathfrom_new1')
                pathfrom2 = data.get('add_pathfrom_new2')
                pathfrom = pathfrom1 + '\\\\' + pathfrom2 + '\\\\XBRL\\\\%mydate%\\\\'
                pathto_temp1 = data.get('add_pathto_temp_new1')
                pathto_temp2 = data.get('add_pathto_temp_new2')
                pathto_temp = pathto_temp1 + '\\' + pathto_temp2 +'\\TEMP\\'
                move1 = data.get('add_move_new1')
                move2 = data.get('add_move_new2')
                move3 = data.get('add_move_new3')
                move = move1 + '\\' + move2 +'\\TEMP\\CN_'+ move3 + '_*zip'
                pathto1 = data.get('add_pathto_new1')
                pathto2 = data.get('add_pathto_new2')
                pathto = pathto1 + '\\' + pathto2 + '\\'
                md1 = data.get('add_md_new1')
                md2 = data.get('add_md_new2')
                md = md1 + '\\' + md2 + '\\'
                mput1 = data.get('add_mput_new1')
                mput2 = data.get('add_mput_new2')
                mput = mput1 + '/' + mput2 + '/'
                send1 = data.get('add_send_new1')
                send2 = data.get('add_send_new2')
                send = send1 + '/' + send2 + '/%mydate%/'
                if_exist1 = data.get('add_if_exist_new1')
                if_exist2 = data.get('add_if_exist_new2')
                if_exist = if_exist1 + '\\' + if_exist2 + '\\CN*' 
                move_file1 = data.get('add_move_file_new1')
                move_file2 = data.get('add_move_file_new2')
                move_file = move_file1 + '_累计\\' + move_file2
            fund = FundModel.objects.create(fundname=fundname, code=fundcode, type=fundtype, is_history=history, pathfrom=pathfrom, pathto_temp=pathto_temp,
                                        move=move, pathto=pathto, md=md, mput=mput, send=send, if_exist=if_exist, move_file=move_file)
            fund.manager = manager
            fund.save()
        if fundtype =='ta':
            pass
        FundItems = FundModel.objects.exclude(is_deleted=True).order_by('fundname')
        return render(request, "stationconfig.html", {'funds':FundItems}) 
    
    
class ModifyFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:fund'))
    
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
        FundItems = FundModel.objects.exclude(is_deleted=True).order_by('fundname')
        return render(request, "stationconfig.html", {'funds':FundItems})
    
    
class DeleteFundView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('stationconfig:fund'))
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        fundid = data.get('delete_fundid')
        FundModel.objects.filter(id=fundid).update(is_deleted=True)
        FundItems = FundModel.objects.exclude(is_deleted=True).order_by('fundname')
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