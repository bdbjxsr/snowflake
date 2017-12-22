#coding:utf-8
#说明：    定义了菜单模块数据
#作者：    万良卿
#时间：    20171123
from django.db import models
from django.db.models import Q

from framework.models.base_model import SnowModel
from framework.models.auth_model import PermissionModel
from framework.models.base_model import SoftDeletionManager
from framework import auth

class MenuItemManager(SoftDeletionManager):
    def __init__(self, *args, **kwargs):
        super(MenuItemManager, self).__init__(*args, **kwargs)
        
    def get_menu(self, request):
        """
        return user menu recurcive max depth 3
        format likes:
        [
          {
            "id": 1, "name": "UserManagment", "code": "um", "url": "/user/manage", "icon": "user",
            "sub_menu": [
              {"id": 1, "name": "UserManagment", "code": "um", "url": "/user/manage", "icon": "user",},
              {"id": 1, "name": "UserManagment", "code": "um", "url": "/user/manage", "icon": "user", "sub_menu": [
                {"id": 1, "name": "UserManagment", "code": "um", "url": "/user/manage", "icon": "user",},
                {"id": 1, "name": "UserManagment", "code": "um", "url": "/user/manage", "icon": "user",},
                {"id": 1, "name": "UserManagment", "code": "um", "url": "/user/manage", "icon": "user",}
                ]},
                ......
            ]
          },
          {
            "id": 1,
            "name": "Appetizers",
            "code":
            "url":
            ......
        ]
        """
        menu_tree = []
        for menu_top in self.get_queryset().filter(parent_menu=None):
            if auth.has_perm(request=request, perm=menu_top.permission):
                menu_temp = {}
                menu_temp['id'] = menu_top.id
                menu_temp['name'] = menu_top.name
                menu_temp['code'] = menu_top.code
                menu_temp['icon'] = menu_top.icon
                menu_temp['url'] = menu_top.url
                menu_temp['sub_menu'] = self._get_child_menu_tree(request=request, menu=menu_top)
                menu_tree.append(menu_temp)
        return menu_tree
    
    def _get_child_menu_tree(self, request, menu):
        menu_tree = []
        for child_menu in self.get_queryset().filter(parent_menu=menu):
            if auth.has_perm(request=request, perm=child_menu.permission):
                menu_temp = {}
                menu_temp['id'] = child_menu.id
                menu_temp['name'] = child_menu.name
                menu_temp['code'] = child_menu.code
                menu_temp['icon'] = child_menu.icon
                menu_temp['url'] = child_menu.url
                menu_temp['sub_menu'] = self._get_child_menu_tree(request=request, menu=child_menu)
                menu_tree.append(menu_temp)
        return menu_tree
        
    def get_queryset(self):
        return super(SoftDeletionManager, self).get_queryset().order_by("sort_seq")

class MenuItemModel(SnowModel):
    #菜单名称
    name = models.CharField(max_length=256, verbose_name='菜单名称')
    #菜单名称
    code = models.CharField(max_length=256, unique=True, verbose_name='菜单代码')
    #菜单地址
    url = models.CharField(max_length=256, verbose_name='菜单地址')
    #图标
    icon = models.CharField(max_length=256, default='ion-briefcase titleIcon icon', verbose_name='菜单地址')
    #排序
    sort_seq = models.IntegerField(verbose_name='菜单地址')
    #关联访问菜单权限
    permission = models.ForeignKey(PermissionModel, null=True, blank=True, on_delete=models.CASCADE)
    #上级菜单（Department-ForeignKey）
    parent_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    objects = MenuItemManager()
    all_objects = MenuItemManager(alive_only=False)
    
    def __str__(self):
        return self.name