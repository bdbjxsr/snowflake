#coding:utf-8
#说明：    定义了认证相关方法
#作者：    万良卿
#时间：    20171114

from .models.auth_model import User

def authenticate(employee_id,password):
    m = Member.objects.get(username=request.POST['username'])    

def login(request, user):
    request.session['employee_id'] = user.employee_id
    print(user.employee_id)
    if hasattr(request, 'user'):
        request.user = user
         
def logout(request):
    try:
        del request.session['employee_id']
    except KeyError:
        pass
    return True