from .mysql import *
from .models import *

# 初始化
from tortoise import Tortoise

async def reg_tortoise(app):
    await Tortoise.init(
        db_url='mysql://root:123654@127.0.0.1:3306/testdb',
        modules={'models': ['sql.models']},
    )
    # Generate the schema
    # await Tortoise.generate_schemas()