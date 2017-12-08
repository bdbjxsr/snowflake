#coding:utf-8
#说明：    定义了认证模块需要的数据模型
#作者：    万良卿
#时间：    20171114
import hashlib
from datetime import datetime


from django.db import models
from django.db.models import Q

from framework.models.base_model import SnowModel


class DepartmentModel(SnowModel):
    #部门名称
    name = models.CharField(max_length=256, verbose_name='部门名称')
    #部门代码
    code = models.CharField(max_length=256, verbose_name='部门代码')
    #部门（Department-ForeignKey）
    super_department = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class UserModel(SnowModel):
    #员工工号
    employee_id = models.CharField(max_length=256, unique=True ,verbose_name='工号')
    #员工姓名
    username = models.CharField(max_length=256, verbose_name='员工姓名')
    #密码
    password = models.CharField(max_length=256, verbose_name='密码')    
    #部门（User-ForeignKey）
    department = models.ForeignKey(DepartmentModel, null=True, blank=True, on_delete=models.CASCADE)
    #上级员工（User-ManyToManyField）
    superiors = models.ManyToManyField('self', related_name='subordinates',)    
    #是否是超级管理员
    is_superuser = models.BooleanField(default=False)
    
    #设置密码 
    def set_password(self, raw_password):
        self.password = hashlib.md5(raw_password.encode('utf-8')).hexdigest()
            
    #验证密码
    def check_password(self, password):
        encoded_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        if encoded_password == self.password:
            return True
        return False
    
    #返回用户组权限的集合
    def get_user_permissions(self, type=None):
        permissions = {}
        for up in self.get_user_user_position():
            for permission in up.position.permissions.all() :
                if not type or permission.type == type: permissions[permission.value] = permission.name
        return permissions
    
    #返回用户代理权限的集合
    def get_temp_permissions(self, type=None):
        permissions = {}
        for up in self.get_temp_user_position():
            for permission in up.position.permissions.all() :
                if not type or permission.type == type: permissions[permission.value] = permission.name
        return permissions
    
    #返回用户所有的权限集合
    def get_all_permissions(self, type=None):
        permissions = {}
        for up in self.get_all_user_position():
            for permission in up.position.permissions.all() :
                if not type or permission.type == type: permissions[permission.value] = permission.name
        return permissions
    
    #返回用户所有的权限集合
    def get_user_position(self):
        return self.position_set.all()
    #返回用户所有的权限集合
    def get_temp_position(self):
        return self.position_set.all()
    #返回用户所有的权限集合
    def get_all_position(self):
        return self.position_set.all()
    
    #返回用户职位
    def get_all_user_position(self):
        return self.get_user_user_position().all() | self.get_temp_user_position().all()
    #返回用户用户临时职位
    def get_temp_user_position(self):
        now = datetime.now()
        return UserPositionModel.objects.filter(user=self, is_authorized=True, start_date__lt=now, expire_date__gt=now)
    #返回用户所有职位
    def get_user_user_position(self):
        return UserPositionModel.objects.filter(user=self, is_authorized=False)

    
    @classmethod
    def create_user(cls, employee_id, username, password):
        """
        create base user infomation
        """
        user = cls(employee_id = employee_id, username = username)
        user.set_password(password)
        user.save()
        return user
    
    def __str__(self):
        return self.username

class PositionModel(SnowModel):
    #所属职位名称
    name = models.CharField(max_length=256, verbose_name='职位名称')
    #职位代码
    code = models.CharField(max_length=256, verbose_name='职位代码')
    #所属部门（Department-ForeignKey）
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    #所属员工（User-ManyToManyField）
    users = models.ManyToManyField(
        UserModel,
        through='UserPositionModel',
        through_fields=('position', 'user'),
        related_name='positions',
    )
    
    def __str__(self):
        return self.name
    
class UserPositionModel(SnowModel):
    #岗位（Position-ForeignKey）
    position = models.ForeignKey(PositionModel, on_delete=models.CASCADE)
    #员工（User-ForeignKey）
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    #是否为代岗（默认为否）
    is_authorized = models.BooleanField(default=False)
    #被代岗人（User-ForeignKey）
    authorizer = models.ForeignKey(
        UserModel,
        null=True, 
        blank=True, 
        on_delete=models.CASCADE,
        related_name="authorizer",
    )
    #代岗原因
    authorize_reason = models.CharField(null=True, blank=True, max_length=64)
    #代岗起始时间
    start_date = models.DateTimeField(null=True, blank=True)
    #代岗截止时间
    expire_date = models.DateTimeField(null=True, blank=True)
    
    class Meta:  
        unique_together = (("position", "user"),)
    def __str__(self):
        return self.position.name+self.user.username
    
class PermissionModel(SnowModel):
    #权限名称描述
    name = models.CharField(max_length=256, verbose_name='权限名称')
    #权限值，作为判断依据，不允许重复
    value = models.CharField(max_length=256, unique=True, verbose_name='权限值')
    #权限类型
    type = models.CharField(max_length=256, verbose_name='权限类型')
    #所属岗位（Position-ManyToManyField）
    positions = models.ManyToManyField(PositionModel, related_name='permissions')
    
    def __str__(self):
        return self.name
    

    
    