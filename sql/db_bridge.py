import asyncio
import concurrent
import traceback
import threading


# 处理orm操作的线程
class DBBridge:
    _instance_lock = threading.Lock()
    _loop = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(DBBridge, "_instance"):
            with DBBridge._instance_lock:
                if not hasattr(DBBridge, "_instance"):
                    DBBridge._instance = object.__new__(cls)
                    DBBridge._instance._loop = asyncio.new_event_loop()
                    DBBridge._instance.start()
        return DBBridge._instance

    def start(self):
        thread = threading.Thread(target=self.run_loop, args=(self._loop,))
        thread.daemon = True
        thread.start()

    def run_loop(self, loop):
        asyncio.set_event_loop(loop)
        self._loop.run_forever()

    def create_task(self, coro, is_return=False):
        future = asyncio.run_coroutine_threadsafe(coro, self._loop)
        if is_return:
            try:
                return future.result(timeout=10)
            except concurrent.futures.TimeoutError:
                print("Task did not complete in time.")
                return None
        return future

    @property
    def loop(self):
        return self._loop
