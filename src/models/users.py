from email.policy import default
from tabnanny import verbose
from tortoise import Model, fields
from .base import BaseModel

class Users(BaseModel):
    name = fields.CharField(50, default='', verbose='姓名')
    mobile = fields.CharField(50, default='', verbose='手机号')
    age = fields.IntField(default=0, verbose='年龄')

    def __str__(self):
        return self.name
    
    class Meta:
        table = "users"