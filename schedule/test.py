import asyncio
import datetime
from sql import User

def tick():
    print('Tick! The time is: %s' % datetime.datetime.now())

async def add_user():
    await User.create(name='张三', id_no='123456789012345678')