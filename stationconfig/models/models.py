#coding:utf-8
#说明：    定义生成配置文件所需变量
#作者：    阙泠伊
#时间：    20180104
from django.db import models

from framework.models.base_model import SnowModel


class TemplateModel(SnowModel):
    #模板名称
    name = models.CharField(max_length=256, verbose_name='模板名称')
    #模板代码
    code = models.CharField(max_length=256, verbose_name='模板代码')
    #版本号
    version = models.CharField(max_length=256, verbose_name='版本号')
    
    def __str__(self):
        return self.username
    
    
class ManagerModel(SnowModel):
    #管理人
    name = models.CharField(max_length=256, verbose_name='管理人')
    #管理人代码
    code = models.CharField(max_length=256, verbose_name='管理人代码', unique=True)

    def __str__(self):
        return self.username

    
class FundModel(SnowModel):
    #基金项目
    fundname = models.CharField(max_length=256, verbose_name='基金名称')
    #基金代码 
    code = models.CharField(max_length=256, verbose_name='基金代码', unique=True)
    #数据类型 
    type = models.CharField(max_length=256, verbose_name='数据类型')
    #管理人代码
    manager = models.ForeignKey(ManagerModel, null=True, blank=True, on_delete=models.CASCADE)
    #是否历史数据
    is_history = models.BooleanField(default=False)
    #GetFile所需变量
    pathfrom = models.CharField(max_length=256)
    pathto_temp = models.CharField(max_length=256)
    move = models.CharField(max_length=256)
    pathto = models.CharField(max_length=256)
    
    #PutFile所需变量
    md = models.CharField(max_length=256)
    mput = models.CharField(max_length=256)
    send = models.CharField(max_length=256)
    
    #文件移动所需变量
    if_exist = models.CharField(max_length=256)
    move_file = models.CharField(max_length=256)
    
    #配置模板
    template_code = models.ForeignKey(TemplateModel, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
    
class SelectManager(models.Model):
    manager = models.ForeignKey(ManagerModel)
    fund = models.ForeignKey(FundModel)
