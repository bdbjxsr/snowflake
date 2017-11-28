#coding:utf-8
#说明：    测试view类，用于测试后端方法
#作者：    万良卿
#时间：    20171122
from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse

from framework.models.auth_model import User, Department, Position, Permission, UserPosition
from framework.models.menu_model import MenuItem
from framework.decorator import login_required
from django.shortcuts import render

@login_required()
def testMethodView(request, method):
    if method == "testMenu":
        mi = MenuItem.objects.get_menu(request)
        for menu in mi.keys():
            print(menu)
        return HttpResponse(mi)
    return HttpResponse(method)

def testPageView(request, method):
    if method == "2":
        return render(request, "framework/test2.html", {})
    else:
        return render(request, "framework/test.html", {})

def initDataView(request, method):
    if not method or method=="":
        return HttpResponse("please enter a explicit method: [all, initUser, initMenu]")
    if method=="initUser" or method=="all" :
#         from framework.models.auth_model import User, Department
#         user = User.create_user(employee_id="161189", username="万良卿", password="00000")
#         department = Department.objects.create(name="科技部")
#         user.department = department
#         user.save()
#         return HttpResponse(user.username)
        dp = Department.objects.create(name="科技部", code="dp_kjb")
        dp1 = Department.objects.create(name="研发一部", code="dp_dev1")
        dp1.super_department = dp
        dp2 = Department.objects.create(name="研发二部", code="dp_dev2")
        dp2.super_department = dp
        dp3 = Department.objects.create(name="研发三部", code="dp_dev3")
        dp3.super_department = dp
        dp4 = Department.objects.create(name="研发四部", code="dp_dev4")
        dp4.super_department = dp
        dp5 = Department.objects.create(name="研发五部", code="dp_dev5")
        dp5.super_department = dp
        
        user1 = User.create_user(employee_id="161186", username="万良卿", password="00000")
        user1.department_id = dp1.id
        user1.is_superuser = True
        user1.save()
        user2 = User.create_user(employee_id="161187", username="万小弟", password="00000")
        user2.department_id = dp1
        user2.superiors.add(user1)
        user2.save()
        user3 = User.create_user(employee_id="161188", username="万大弟", password="00000")
        user3.department_id = dp2
        user3.superiors.add(user1)
        user3.save()
        
        position1 = Position.objects.create(name="一部_经理", department=dp1, code="pt_manange1")
        position2 = Position.objects.create(name="一部_开发岗", department=dp1, code="pt_dev1")
        position3 = Position.objects.create(name="二部_经理", department=dp2, code="pt_manange2")
        position4 = Position.objects.create(name="二部_开发岗", department=dp2, code="pt_dev2")
        
        permission = Permission.objects.create(name="可以开发", value="can_program", type="1")
        permission.positions.add(position2, position4)
        permission = Permission.objects.create(name="可以管理", value="can_manage", type="1")
        permission.positions.add(position1, position3)
        
        UserPosition.objects.create(position=position1, user=user1)
        UserPosition.objects.create(position=position2, user=user1)
        UserPosition.objects.create(position=position2, user=user2)
        UserPosition.objects.create(position=position3, user=user3)
        UserPosition.objects.create(position=position4, user=user3)
        start_date = datetime.strptime('2017-11-21 15:01:28', '%Y-%m-%d %H:%M:%S')
        expire_date = datetime.strptime('2017-12-21 15:01:28', '%Y-%m-%d %H:%M:%S')
        UserPosition.objects.create(position=position3, user=user1, is_authorized=True, authorizer=user3, 
                                    authorize_reason="测试代理经理岗位",start_date=start_date, expire_date=expire_date)
        
        start_date = datetime.strptime('2017-11-21 15:01:28', '%Y-%m-%d %H:%M:%S')
        expire_date = datetime.strptime('2017-11-22 15:01:28', '%Y-%m-%d %H:%M:%S')
        UserPosition.objects.create(position=position4, user=user1, is_authorized=True, authorizer=user3, 
                                    authorize_reason="测试代理研发岗位",start_date=start_date, expire_date=expire_date)
        
    if method == "initMenu" or method=="all":
        permission1 = Permission.objects.create(name="测试页面1权限", value="page_test_1", type="2")
        permission2 = Permission.objects.create(name="测试页面1权限", value="page_test_2", type="2")
        permission3 = Permission.objects.create(name="测试页面1权限", value="page_test_3", type="2")
        mi1 = MenuItem.objects.create(name="测试页面1", code="test_menu_1", icon ='ion-speedometer', sort_seq=0, url="www.baidu.com")
        mi2 = MenuItem.objects.create(name="测试页面2", code="test_menu_2", icon ='ion-ios-world', sort_seq=1, url="www.baidu.com", permission=permission1, parent_menu=mi1)
        mi3 = MenuItem.objects.create(name="测试页面3", code="test_menu_3", icon ='ion-mouse', sort_seq=0, url="www.baidu.com", permission=permission2, parent_menu=mi1)
        mi4 = MenuItem.objects.create(name="测试页面4", code="test_menu_4", icon ='ion-briefcase', sort_seq=1, url="www.baidu.com", permission=permission3)
        
        position1 = Position.objects.get(code="pt_manange1")
        position2 = Position.objects.get(code="pt_dev2")
        
        position1.permissions.add(permission1, permission3)
        position2.permissions.add(permission2)
        
    return HttpResponse("excute success")

