#coding:utf-8
#说明：    定义了认证相关方法
#作者：    万良卿
#时间：    20171114

from .models.auth_model import User
import hashlib

def authenticate(employee_id,password):
    try:
        m = User.objects.get(employee_id=employee_id)
        db_password = m.password
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        if password == db_password:
            user = {}
            print("111")
            return True
    except :
        print("员工号不存在或密码错误，请重新输入！")
    

def login(request, employee_id):
    request.session['employee_id'] = employee_id
    print(employee_id)
    if hasattr(request, 'employee_id'):
        #request.user = user
        return True
         
def logout(request):
    try:
        del request.session['employee_id']
    except KeyError:
        pass
    return True