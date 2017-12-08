#coding:utf-8
#说明：    基础数据模型用于模型，实现软删除
#作者：    万良卿
#时间：    20171114
from django.db import models

#软删除model
class SoftDeletionQuerySet(models.QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(is_deleted=True)

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(is_deleted=False)

    def dead(self):
        return self.exclude(is_deleted=False)

class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(is_deleted=False)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()   


class SnowModel(models.Model):
    #通用表字段
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super(SnowModel, self).delete()
        
        
