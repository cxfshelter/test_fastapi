import asyncio
import datetime
from sql import User, db_bridge

def tick():
    print('Tick! The time is: %s' % datetime.datetime.now())

async def add_user():
    async def test():
        print(f'start add user')
        return await User.create(name='张三', id_no='123456789012345678')

    db_bridge.create_task(test(), is_return=True)