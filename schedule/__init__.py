from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

from apscheduler.schedulers.asyncio import AsyncIOScheduler
io_scheduler = AsyncIOScheduler()

from .test import *