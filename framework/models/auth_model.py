#coding:utf-8
#说明：    定义了认证模块需要的数据模型
#作者：    万良卿
#时间：    20171114
from django.db import models

from .base_model import SnowModel, SoftDeletionManager
import hashlib

class UserManager(SoftDeletionManager):
 
    def create_user(self, employee_id, username, department_id , superior, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not employee_id:
            raise ValueError('Users must have an employee_id')
        
        
        user = self.model(
            employee_id = employee_id,
            username = username,
            department_id = department_id,
            password = hashlib.md5('nbcb'.encode('utf-8')).hexdigest()
             )
        user.save(using=self._db)
        User.objects.get(employee_id=employee_id).superior.add(superior)
        return user 

class Department(SnowModel):    
    name = models.CharField(max_length=256, verbose_name='部门名称')
    #部门（Department-ForeignKey）
    super_department = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

class User(SnowModel):
    #员工工号
    employee_id = models.CharField(max_length=256, unique=True ,verbose_name='工号')
    #员工姓名
    username = models.CharField(max_length=256, verbose_name='员工姓名')
    #密码
    password = models.CharField(max_length=256, verbose_name='密码')
    
    #部门（User-ForeignKey）
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #上级员工（User-ManyToManyField）
    superior = models.ManyToManyField('self')
    
    objects = UserManager()
        
    def set_password(self, raw_password):
        pass
    
    def check_password(self, raw_password):
        pass

class Position(SnowModel):
    #所属部门（Department-ForeignKey）
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #所属员工（User-ManyToManyField）
    users = models.ManyToManyField(
        User,
        through='UserPosition',
        through_fields=('position', 'user'),
    )
    
class UserPosition(SnowModel):
    #岗位（Position-ForeignKey）
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    #员工（User-ForeignKey）
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #是否为代岗（默认为否）
    is_authorized = models.BooleanField(default=False)
    #被代岗人（User-ForeignKey）
    authorizer = models.ForeignKey(
        User,
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
    
class Permission(SnowModel):
    #权限名称
    name = models.CharField(max_length=256, verbose_name='权限名称')
    #权限类型
    type = models.CharField(max_length=256, verbose_name='权限类型')
    #所属岗位（Position-ManyToManyField）
    position = models.ManyToManyField(Position)
    

    
    