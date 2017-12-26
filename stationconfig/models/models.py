from django.db import models

class StationConfigModel(SnowModel):
    #部门名称
    name = models.CharField(max_length=256, verbose_name='部门名称')
    #部门代码
    code = models.CharField(max_length=256, verbose_name='部门代码')
    #部门（Department-ForeignKey）
    super_department = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name