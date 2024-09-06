import asyncio

async def my_coroutine():
    print("开始执行协程")
    await asyncio.sleep(1)
    print("协程执行完毕")

# 创建一个事件循环
loop = asyncio.get_event_loop()

# 使用 run_until_complete 运行协程
loop.run_until_complete(my_coroutine())

# 关闭事件循环
loop.close()