from django.conf.urls import url

from stationconfig.views import views, test_view

app_name = 'stationconfig'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    url(r'^manage$', views.ManageView.as_view(), name='manage'),
    url(r'^search$', views.SearchFundView.as_view(), name='search'),
    url(r'^add$', views.AddFundView.as_view(), name='add'),
    url(r'^modify$', views.ModifyFundView.as_view(), name='modify'),
    url(r'^delete$', views.DeleteFundView.as_view(), name='delete'),
    
    url(r'^select_manager$', views.SelectManager.as_view(), name='select_manager'),
    url(r'^manager/query/json$', views.QueryJsonManagerView.as_view(), name='query_json_manager'),
    url(r'^fund/query/json/(?P<manager>.*)$', views.QueryJsonFundView.as_view(), name='query_json_fund'),
    
    url(r'^export_getfile', views.ExportGetFile.as_view(), name='export_getfile'),
    url(r'^export_putfile', views.ExportPutFile.as_view(), name='export_putfile'),
    url(r'^export_movefile', views.ExportMoveFile.as_view(), name='export_movefile'),
    
    url(r'^test/initdata/(?P<method>.*)$', test_view.InitDataView.as_view(), name='test_initdata'),
]