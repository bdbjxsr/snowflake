#coding:utf-8
#说明：    定义了认证相关方法
#作者：    万良卿
#时间：    20171114
from django.utils import six

from framework.models.auth_model import User

def authenticate(employee_id, password):
    try:
        user = User.objects.get(employee_id=employee_id)
        if user.check_password(password):
            return user
    except :
        return False    

def login(request, user):
    request.session['employee_id'] = user.employee_id
    request.session['permissions'] = user.get_all_permissions()
    if hasattr(request, 'employee_id'):
        return True
    
def has_perm(request, perm):
    if request.user.is_superuser:
        return True
    if not perm:
        return True
    if request.session.has_key('permissions'):
        if isinstance(perm, six.string_types):
            perms = (perm, )
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        for p in perms:
            if  p not in request.session['permissions'].keys():
                return False
        return True
    return False
         
def logout(request):
    try:
        del request.session['employee_id']
    except KeyError:
        pass
    return True