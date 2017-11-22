from django.conf.urls import url

from framework.views import auth_view, test_view

app_name = 'framework'
urlpatterns = [
    url(r'^$', auth_view.index, name='index'),
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^logout/$', auth_view.logout, name='logout'),
    url(r'^permission/denied/$', auth_view.permissionDenied, name='permissionDenied'),
    url(r'^test/$', test_view.testView, name='testView'),
    url(r'^test/regiest/$', test_view.testRegiestUser, name='testRegiestUser'),
    url(r'^test/positon/$', test_view.testPositon, name='testPositon'),
]