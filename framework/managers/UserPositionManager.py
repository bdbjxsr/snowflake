#coding:utf-8
#说明：    定义了认证模块需要的数据模型
#作者：    万良卿
#时间：    20171121
from datetime import datetime

from django.db.models import Q

from framework.models.base_model import SoftDeletionManager


class UserPositionManager(SoftDeletionManager):
    def __init__(self, *args, **kwargs):
        super(UserPositionManager, self).__init__(*args, **kwargs)
        
    def get_queryset(self):
        now = datetime.now()
        return super(SoftDeletionManager, self).get_queryset().filter(
                (Q(is_authorized=True) & Q(start_date__lt=now) & Q(expire_date__gt=now)) |
                (Q(is_authorized=False))
                )
    