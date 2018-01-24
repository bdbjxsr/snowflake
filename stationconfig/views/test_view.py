#coding:utf-8
#说明：    测试view类，用于测试后端方法
#作者：    阙泠伊
#时间：    20180104
from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.shortcuts import render

from stationconfig.models.models import TemplateModel, FundModel, ManagerModel

class InitDataView(View):
    def get(self, request, method, *args, **kwargs):
        if not method or method=="":
            return HttpResponse("please enter a explicit method: [all, initFund]")
            
        if method=="initFund" or method=="all" :
            manager1 = ManagerModel.objects.create(name="金元惠理", code="k0058")
            manager1.save()
            manager2 = ManagerModel.objects.create(name="国泰基金", code="k0043")
            manager2.save()
            manager3 = ManagerModel.objects.create(name="银华基金", code="k0013")
            manager3.save()
            manager4 = ManagerModel.objects.create(name="安信基金", code="k0079")
            manager4.save()
            manager5 = ManagerModel.objects.create(name="博时基金", code="k0052")
            manager5.save()
             
            fund1 = FundModel.objects.create(fundname="金元宝货币", type="xbrl", is_history=True, pathfrom="k0058\\\\金元惠理\\\\%mydate%\\\\",
                                             pathto_temp="金元宝货币\\TEMP\\", move="金元宝货币\\TEMP\\CN*zip", pathto="金元宝货币\\", md="金元宝货币\\",
                                             mput="金元宝货币/", send="k0058/金元惠理/%mydate%/", if_exist="金元宝货币\\CN*", move_file="金元宝货币_累计")
            fund1.manager = manager1
            fund1.save()
            fund2 = FundModel.objects.create(fundname="国泰基金淘金", type="xbrl", is_history=True, pathfrom="k0043\\\\国泰基金\\\\%mydate%\\\\",
                                             pathto_temp="国泰基金\\TEMP\\", move="国泰基金\\TEMP\\CN*zip", pathto="国泰基金\\", md="国泰基金\\",
                                             mput="国泰基金/", send="k0043/国泰基金/%mydate%/", if_exist="国泰基金\\CN*", move_file="国泰基金_累计")
            fund2.manager = manager2
            fund2.save()
            fund3 = FundModel.objects.create(fundname="银华基金", type="xbrl", is_history=True, pathfrom="k0013\\\\XBRL\\\\%mydate%\\\\",
                                             pathto_temp="银华基金\\TEMP\\", move="银华基金\\TEMP\\*", pathto="银华基金\\", md="银华基金\\",
                                             mput="银华基金/", send="k0013/XBRL/%mydate%/", if_exist="银华基金\\CN*", move_file="银华基金_累计")
            fund3.manager = manager3
            fund3.save()
            fund4 = FundModel.objects.create(fundname="安信基金", code="001399", type="xbrl", is_history=True, pathfrom="k0079\\\\XBRL\\\\%mydate%\\\\",
                                             pathto_temp="安信基金\\TEMP\\", move="安信基金\\TEMP\\CN_50700000_001399*", pathto="安信基金\\", md="安信基金\\",
                                             mput="安信基金/", send="k0079/XBRL/%mydate%/", if_exist="安信基金\\CN*", move_file="安信基金_累计")
            fund4.manager = manager4
            fund4.save()
            fund5 = FundModel.objects.create(fundname="博时裕晟", code="002008", type="xbrl", is_history=True, pathfrom="k0052\\\\博时基金\\\\%mydate%\\\\xbrl\\\\",
                                             pathto_temp="博时基金\\博时裕晟\\TEMP\\", move="博时基金\\博时裕晟\\TEMP\\CN_50050000_002008*zip", pathto="博时基金\\博时裕晟\\", 
                                             md="博时基金\\博时裕晟\\", mput="博时基金/博时裕晟/", send="k0052/博时基金/%mydate%/", if_exist="博时基金\\博时裕晟\\CN*",
                                             move_file="博时基金_累计\\博时裕晟")
            fund5.manager = manager5
            fund5.save()
            fund6 = FundModel.objects.create(fundname="博时裕顺", code="002811", type="xbrl", is_history=True, pathfrom="k0052\\\\博时基金\\\\%mydate%\\\\xbrl\\\\",
                                             pathto_temp="博时基金\\博时裕顺\\TEMP\\", move="博时基金\\博时裕顺\\TEMP\\CN_50050000_002811*zip", pathto="博时基金\\博时裕顺\\", 
                                             md="博时基金\\博时裕顺\\", mput="博时基金/博时裕顺/", send="k0052/博时基金/%mydate%/", if_exist="博时基金\\博时裕顺\\CN*",
                                             move_file="博时基金_累计\\博时裕顺")
            fund6.manager = manager5
            fund6.save()
            return HttpResponse("excute success")