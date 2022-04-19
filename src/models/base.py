from tortoise import Model, fields

class BaseModel(Model):
    id = fields.IntField(pk=True, verbose='姓名')
    created = fields.DatetimeField(null=False, verbose='创建时间')