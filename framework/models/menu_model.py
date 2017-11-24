#coding:utf-8
#说明：    定义了菜单模块数据
#作者：    万良卿
#时间：    20171123
from django.db import models
from django.db.models import Q

from framework.models.base_model import SnowModel
from framework.models.auth_model import Permission
from framework.models.base_model import SoftDeletionManager

class MenuItemManager(SoftDeletionManager):
    def __init__(self, *args, **kwargs):
        super(UserPositionManager, self).__init__(*args, **kwargs)
        
    def get_queryset(self):
        now = datetime.now()
        return super(SoftDeletionManager, self).get_queryset().order_by("sort_seq")

class MenuItem(SnowModel):
    #菜单名称
    name = models.CharField(max_length=256, verbose_name='菜单名称')
    #菜单名称
    code = models.CharField(max_length=256, unique=True, verbose_name='菜单代码')
    #菜单地址
    url = models.CharField(max_length=256, verbose_name='菜单地址')
    #排序
    sort_seq = models.IntegerField(verbose_name='菜单地址')
    #关联访问菜单权限
    permission = models.ForeignKey(Permission, null=True, blank=True, on_delete=models.CASCADE)
    #上级菜单（Department-ForeignKey）
    parent_menu = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)
    
    def __str__(self):
        return self.name