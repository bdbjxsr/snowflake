#coding:utf-8
#说明：    定义了菜单模块数据
#作者：    万良卿
#时间：    20171123
from django.db import models
from django.db.models import Q

from framework.models.base_model import SnowModel
from framework.models.auth_model import Permission
from framework.models.base_model import SoftDeletionManager
from framework import auth

class MenuItemManager(SoftDeletionManager):
    def __init__(self, *args, **kwargs):
        super(MenuItemManager, self).__init__(*args, **kwargs)
        
    def get_menu(self, request):
        menu_tree = {}
        for top_menu in self.get_queryset().filter(parent_menu=None):
            if auth.has_perm(request=request, perm=top_menu.permission):
                menu_tree[top_menu] = self._get_child_menu_tree(request=request, menu=top_menu)
        return menu_tree
    
    def _get_child_menu_tree(self, request, menu):
        menu_tree = {}
        for child_menu in self.get_queryset().filter(parent_menu=menu):
            if auth.has_perm(request=request, perm=child_menu.permission):
                menu_tree[child_menu] = self._get_child_menu_tree(request=request, menu=child_menu)
        return menu_tree
        
    def get_queryset(self):
        return super(SoftDeletionManager, self).get_queryset().order_by("sort_seq")

class MenuItem(SnowModel):
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
    permission = models.ForeignKey(Permission, null=True, blank=True, on_delete=models.CASCADE)
    #上级菜单（Department-ForeignKey）
    parent_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    objects = MenuItemManager()
    all_objects = MenuItemManager(alive_only=False)
    
    def __str__(self):
        return self.name