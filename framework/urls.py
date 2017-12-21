from django.conf.urls import url

from framework.views import auth_view, test_view, admin_view

app_name = 'framework'
urlpatterns = [
    url(r'^$', auth_view.IndexView.as_view(), name='index'),
    url(r'^auth/login/$', auth_view.LoginView.as_view(), name='auth_login'),
    url(r'^auth/logout/$', auth_view.LogoutView.as_view(), name='auth_logout'),
    url(r'^auth/permission/denied/$', auth_view.DenyPermissionView.as_view(), name='auth_deny_permission'),
    
    url(r'^admin/page/manage$', admin_view.ManageMenuPageView.as_view(), name='admin_page_manage'),
    url(r'^admin/page/add$', admin_view.AddMenuPageView.as_view(), name='admin_page_add'),
    url(r'^admin/position/query/json$', admin_view.QueryJsonPermissionView.as_view(), name='query_json_permission'),
    
    url(r'^admin/user/manage$', admin_view.ManageUserView.as_view(), name='user_manage'),
    url(r'^admin/user/search$', admin_view.SearchUserView.as_view(), name='user_search'),
    url(r'^admin/user/add$', admin_view.AddUserView.as_view(), name='user_add'),
    url(r'^admin/department/query/json$', admin_view.QueryJsonDepartmentView.as_view(), name='query_json_department'),
    url(r'^admin/superdepartment/query/json$', admin_view.QueryJsonSuperDepartmentView.as_view(), name='query_json_superdepartment'),
    
    url(r'^test/testpage/(?P<method>.*)$', test_view.TestPageView.as_view(), name='test_page'),
    url(r'^test/initdata/(?P<method>.*)$', test_view.InitDataView.as_view(), name='test_initdata'),
    url(r'^test/method/(?P<method>.*)$', test_view.TestMethodView.as_view(), name='test_method'),
    
    
]