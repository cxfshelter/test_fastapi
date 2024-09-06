from tortoise import Model, fields

class User(Model):
    """ 用户基础信息 """
    name = fields.CharField(max_length=24, description="姓名")
    id_no = fields.CharField(max_length=24, description="身份证号")

