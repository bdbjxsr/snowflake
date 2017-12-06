from django.conf.urls import url

from framework.views import auth_view, test_view, admin_view

app_name = 'framework'
urlpatterns = [
    url(r'^$', auth_view.index, name='index'),
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^logout/$', auth_view.logout, name='logout'),
    url(r'^permission/denied/$', auth_view.permissionDenied, name='permissionDenied'),
    url(r'^admin/page_manage/$', admin_view.pageManageView, name='pageManage'),
    url(r'^admin/page_manage/add$', admin_view.pageManageAddView, name='pageManageAdd'),
    url(r'^admin/position/query$', admin_view.queryPermissionJson, name='queryPermissionJson'),
    url(r'^test/testPage/(?P<method>.*)$', test_view.testPageView, name='testPage'),
    url(r'^test/initData/(?P<method>.*)$', test_view.initDataView, name='initData'),
    url(r'^test/testMethod/(?P<method>.*)$', test_view.testMethodView, name='testMethod'),
]