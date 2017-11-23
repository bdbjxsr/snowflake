from django.utils.deprecation import MiddlewareMixin

from framework.models.auth_model import User

class Auth(MiddlewareMixin):
    def process_request(self,request):
        if request.session.has_key('employee_id'):
            print(request.session['employee_id'])
            request.user = User.objects.get(employee_id = request.session['employee_id'])
            
    def process_view(self,request):
        pass

    def process_exception(self,request):
        pass

    def process_response(self,request):
        pass
    