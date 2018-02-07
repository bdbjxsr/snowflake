from django.conf.urls import url

from stationconfig.views import fund_view, manager_view, test_view

app_name = 'stationconfig'
urlpatterns = [
    url(r'^fund$', fund_view.FundView.as_view(), name='fund'),
    url(r'^fund/search$', fund_view.SearchFundView.as_view(), name='search_fund'),
    url(r'^fund/add$', fund_view.AddFundView.as_view(), name='add_fund'),
    url(r'^fund/modify$', fund_view.ModifyFundView.as_view(), name='modify_fund'),
    url(r'^fund/delete$', fund_view.DeleteFundView.as_view(), name='delete_fund'),
    
    url(r'^select_manager$', fund_view.SelectManager.as_view(), name='select_manager'),
    url(r'^manager/query/json$', fund_view.QueryJsonManagerView.as_view(), name='query_json_manager'),
    url(r'^fund/query/json/(?P<manager>.*)$', fund_view.QueryJsonFundView.as_view(), name='query_json_fund'),
    
    url(r'^export_getfile', fund_view.ExportGetFile.as_view(), name='export_getfile'),
    url(r'^export_putfile', fund_view.ExportPutFile.as_view(), name='export_putfile'),
    url(r'^export_movefile', fund_view.ExportMoveFile.as_view(), name='export_movefile'),
    
    
    
    
    url(r'^manager$', manager_view.ManagerView.as_view(), name='manager'),
    url(r'^manager/search$', manager_view.SearchManagerView.as_view(), name='search_manager'),
    url(r'^manager/add$', manager_view.AddManagerView.as_view(), name='add_manager'),
    url(r'^manager/modify$', manager_view.ModifyManagerView.as_view(), name='modify_manager'),
    url(r'^manager/delete$', manager_view.DeleteManagerView.as_view(), name='delete_manager'),
    url(r'^manager_code/query/json$', manager_view.QueryJsonManagerCodeView.as_view(), name='query_json_manager_code'),
    
    url(r'^test/initdata/(?P<method>.*)$', test_view.InitDataView.as_view(), name='test_initdata'),
]