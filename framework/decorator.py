#coding:utf-8
#说明：    装饰器
#作者：    万良卿
#时间：    20171115
from functools import wraps


from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.utils import six


def user_passes_test(test_func, redirect_url):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request):
                return view_func(request, *args, **kwargs)
            return HttpResponseRedirect(redirect_url)
        return _wrapped_view
    return decorator


def login_required(redirect_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    def check_login(request):
        if request.session.has_key('employee_id'):
            return True
        return False
    
    return user_passes_test(check_login, redirect_url=redirect_url or settings.LOGIN_URL)

def manager_required(user, redirect_url=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    def check_manager(request):
        if request.user.has_key('employee_id'):
            return True
        return False
    
    return user_passes_test(check_login, redirect_url=redirect_url or settings.LOGIN_URL)


def permission_required(perm, redirect_url=None):
    """
    Decorator for views that checks whether a user has a particular permission
    enabled, redirecting to the log-in page if necessary.
    If the raise_exception parameter is given the PermissionDenied exception
    is raised.
    """
    def check_perms(request):
        if isinstance(perm, six.string_types):
            perms = (perm, )
        else:
            perms = perm
        # First check if the user has the permission (even anon users)
        for p in perms:
            if  p not in request.session['permissions'].keys():
                return False
        return True
    
    return user_passes_test(check_perms, redirect_url=redirect_url or settings.REDIRECT_URL)
