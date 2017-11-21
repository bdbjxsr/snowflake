from django.conf.urls import url

from .views import auth_view

app_name = 'framework'
urlpatterns = [
    url(r'^$', auth_view.index, name='index'),
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^logout/$', auth_view.logout, name='logout'),
    url(r'^permission/denied/$', auth_view.permissionDenied, name='permissionDenied'),
]