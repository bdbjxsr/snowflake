from django.utils.deprecation import MiddlewareMixin

from framework.models.auth_model import UserModel

class Auth(MiddlewareMixin):
    def process_request(self,request):
        if request.session.has_key('employee_id'):
            print(request.session['employee_id'])
            request.user = UserModel.objects.get(employee_id = request.session['employee_id'])


