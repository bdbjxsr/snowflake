from django.conf.urls import url

from stationconfig.views import views

app_name = 'stationconfig'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    
]