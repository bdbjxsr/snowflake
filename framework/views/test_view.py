#coding:utf-8
#说明：    测试view类，用于测试后端方法
#作者：    万良卿
#时间：    20171122
from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.utils.decorators import method_decorator

from framework.models.auth_model import UserModel, DepartmentModel, PositionModel, PermissionModel, UserPositionModel
from framework.models.menu_model import MenuItemModel
from framework.decorator import login_required
from django.shortcuts import render

class TestMethodView(View):
    def get(self, request, method, *args, **kwargs):
        if method == "testMenu":
            mi = MenuItemModel.objects.get_menu(request)
            for menu in mi.keys():
                print(menu)
            return HttpResponse(mi)
        if method == "test_menu_3":
            return render(request, "framework/test.html", {})
        return HttpResponse(method)
    
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class TestPageView(View):
    def get(self, request, method, *args, **kwargs):
        if method == "test_menu_3":
            return render(request, "framework/test.html", {})
        else:
            return HttpResponse(method)

class InitDataView(View):
    def get(self, request, method, *args, **kwargs):
        if not method or method=="":
            return HttpResponse("please enter a explicit method: [all, initUser, initMenu]")
        if method=="initUser" or method=="all" :
    #         from framework.models.auth_model import User, Department
    #         user = User.create_user(employee_id="161189", username="万良卿", password="00000")
    #         department = Department.objects.create(name="科技部")
    #         user.department = department
    #         user.save()
    #         return HttpResponse(user.username)
            dp = DepartmentModel.objects.create(name="科技部", code="dp_kjb")
            dp1 = DepartmentModel.objects.create(name="研发一部", code="dp_dev1")
            dp1.super_department = dp
            dp1.save()
            dp2 = DepartmentModel.objects.create(name="研发二部", code="dp_dev2")
            dp2.super_department = dp
            dp3 = DepartmentModel.objects.create(name="研发三部", code="dp_dev3")
            dp3.super_department = dp
            dp4 = DepartmentModel.objects.create(name="研发四部", code="dp_dev4")
            dp4.super_department = dp
            dp5 = DepartmentModel.objects.create(name="研发五部", code="dp_dev5")
            dp5.super_department = dp
            
            user1 = UserModel.create_user(employee_id="161186", username="万良卿", password="00000")
            user1.department_id = dp1.id
            user1.is_superuser = True
            user1.save()
            user2 = UserModel.create_user(employee_id="161187", username="万小弟", password="00000")
            user2.department = dp1
            user2.superiors.add(user1)
            user2.save()
            user3 = UserModel.create_user(employee_id="161188", username="万大弟", password="00000")
            user3.department = dp2
            user3.superiors.add(user1)
            user3.save()
            
            position1 = PositionModel.objects.create(name="一部_经理", department=dp1, code="pt_manange1")
            position2 = PositionModel.objects.create(name="一部_开发岗", department=dp1, code="pt_dev1")
            position3 = PositionModel.objects.create(name="二部_经理", department=dp2, code="pt_manange2")
            position4 = PositionModel.objects.create(name="二部_开发岗", department=dp2, code="pt_dev2")
            
            permission = PermissionModel.objects.create(name="可以开发", value="can_program", type="1")
            permission.positions.add(position2, position4)
            permission = PermissionModel.objects.create(name="可以管理", value="can_manage", type="1")
            permission.positions.add(position1, position3)
            
            UserPositionModel.objects.create(position=position1, user=user1)
            UserPositionModel.objects.create(position=position2, user=user1)
            UserPositionModel.objects.create(position=position2, user=user2)
            UserPositionModel.objects.create(position=position3, user=user3)
            UserPositionModel.objects.create(position=position4, user=user3)
            start_date = datetime.strptime('2017-11-21 15:01:28', '%Y-%m-%d %H:%M:%S')
            expire_date = datetime.strptime('2017-12-21 15:01:28', '%Y-%m-%d %H:%M:%S')
            UserPositionModel.objects.create(position=position3, user=user1, is_authorized=True, authorizer=user3, 
                                        authorize_reason="测试代理经理岗位",start_date=start_date, expire_date=expire_date)
            
            start_date = datetime.strptime('2017-11-21 15:01:28', '%Y-%m-%d %H:%M:%S')
            expire_date = datetime.strptime('2017-11-22 15:01:28', '%Y-%m-%d %H:%M:%S')
            UserPositionModel.objects.create(position=position4, user=user1, is_authorized=True, authorizer=user3, 
                                        authorize_reason="测试代理研发岗位",start_date=start_date, expire_date=expire_date)
            
        if method == "initMenu" or method=="all":
            permission1 = PermissionModel.objects.create(name="测试页面1权限", value="page_test_1", type="2")
            permission2 = PermissionModel.objects.create(name="测试页面1权限", value="page_test_2", type="2")
            permission3 = PermissionModel.objects.create(name="测试页面1权限", value="page_test_3", type="2")
            mi1 = MenuItemModel.objects.create(name="测试页面1", code="test_menu_1", icon='ion-speedometer', sort_seq=0, url="www.baidu.com")
            mi2 = MenuItemModel.objects.create(name="测试页面2", code="test_menu_2", icon='ion-ios-world', sort_seq=1, url="www.baidu.com", permission=permission1, parent_menu=mi1)
            mi3 = MenuItemModel.objects.create(name="测试页面3", code="test_menu_3", icon='ion-mouse', sort_seq=0, url="www.baidu.com", permission=permission2, parent_menu=mi1)
            mi4 = MenuItemModel.objects.create(name="测试页面4", code="test_menu_4", icon='ion-briefcase', sort_seq=1, url="www.baidu.com", permission=permission3)
            
            
            position1 = PositionModel.objects.get(code="pt_manange1")
            position2 = PositionModel.objects.get(code="pt_dev2")
            
            position1.permissions.add(permission1, permission3)
            position2.permissions.add(permission2)
            
        if method =="user_manage_1":
           # mi5 = MenuItemModel.objects.create(name="用户管理页面", code="user_manage", icon='ion-mouser', sort_seq=5, url="framework:user_manage")
            dp = DepartmentModel.objects.filter(code="dp_kjb")
            for dp_temp in DepartmentModel.objects.all():
                if dp_temp.code !="dp_kjb":
                    dp_temp.super_department = dp[0]
                    dp_temp.save()
                    
            dp5 = DepartmentModel.objects.filter(code="dp_dev5")[0]
            
            user1 = UserModel.create_user(employee_id="060001", username="倪肖勇", password="00000")
            user1.department_id = dp5.id
            user1.save()
            
            user2 = UserModel.create_user(employee_id="170001", username="王仕元", password="00000")
            user2.department = dp5
            user2.superiors.add(user1)
            user2.save()
            user3 = UserModel.create_user(employee_id="170002", username="蔡钟乐", password="00000")
            user3.department = dp5
            user3.superiors.add(user1)
            user3.save()
            user4 = UserModel.create_user(employee_id="170003", username="罗丁拓", password="00000")
            user4.department = dp5
            user4.superiors.add(user1)
            user4.save()
            user5 = UserModel.create_user(employee_id="170004", username="李灵泽", password="00000")
            user5.department = dp5
            user5.superiors.add(user1)
            user5.save()
            user6 = UserModel.create_user(employee_id="170005", username="过伟荣", password="00000")
            user6.department = dp5
            user6.superiors.add(user1)
            user6.save()
            user7 = UserModel.create_user(employee_id="170006", username="冯乐乐", password="00000")
            user7.department = dp5
            user7.superiors.add(user1)
            user7.save()
            user8 = UserModel.create_user(employee_id="170007", username="阙泠伊", password="00000")
            user8.department = dp5
            user8.superiors.add(user1)
            user8.save()
            user9 = UserModel.create_user(employee_id="170008", username="刘志祥", password="00000")
            user9.department = dp5
            user9.superiors.add(user1)
            user9.save()
            
        if method =="user_manage_2":
            user1 = UserModel.objects.filter(employee_id="161186")[0]
            user2 = UserModel.objects.filter(employee_id="170001")[0]
            user2.superiors.add(user1)
            user2.save()
            user3 = UserModel.objects.filter(employee_id="170007")[0]
            user3.superiors.add(user1)
            user3.save()
            
        if method =="dprt_manage_1":
            dp = DepartmentModel.objects.create(name="营业部", code="dp_yyb")
            dp1 = DepartmentModel.objects.create(name="运营一部", code="dp_yyb1")
            dp1.super_department = dp
            dp1.save()
            dp2 = DepartmentModel.objects.create(name="运营二部", code="dp_yyb2")
            dp2.super_department = dp
            dp2.save()
            user1 = UserModel.objects.get(employee_id="170005")
            user1.department = dp1
            user1.save()
            user2 = UserModel.objects.get(employee_id="170006")
            user2.department = dp2
            user2.save() 
        return HttpResponse("excute success")

