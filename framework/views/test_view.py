#coding:utf-8
#说明：    测试view类，用于测试后端方法
#作者：    万良卿
#时间：    20171121
from django.http import HttpResponseRedirect, HttpResponse



def testRegiestUser(request):
#     from framework.models.auth_model import User, Department
#     user = User.create_user(employee_id="161189", username="万良卿", password="00000")
#     department = Department.objects.create(name="科技部")
#     user.department = department
#     user.save()
#     return HttpResponse(user.username)
    from framework.models.auth_model import User, Department, Position, Permission, UserPosition
    user = User.create_user(employee_id="161192", username="万良卿", password="00000")
    user.department_id = "1"
    user.save()
    position = Position.objects.create(name="科技部_开发岗", department_id="1")
    up = UserPosition.objects.create(position=position, user=user)
    
    permission = Permission.objects.create(name="可以开发", value="can_program", type="1")
    permission.positions.add(position)
    position.permission_set.all()
    user.position_set.all()
    return HttpResponse(user.username)