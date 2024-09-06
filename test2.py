import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

async def startup_event():
    print('startup_event')
    from sql import reg_tortoise
    await reg_tortoise(app)

    from schedule import scheduler, io_scheduler, tick, add_user
    io_scheduler.add_job(tick, 'interval', seconds=3)
    io_scheduler.add_job(add_user, 'interval', seconds=10)
    io_scheduler.start()


async def shutdown_event():
    print('shutdown_event')

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_event()
    yield
    await shutdown_event()
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/test/{id}')
async def test(id: int):
    return {'id': id}

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")  # 指定模板目录
@app.get('/showall', response_class=HTMLResponse)
async def showall():
    from sql import User
    users = await User.all()
    return templates.TemplateResponse("users.html", {"request": {}, "users": users})


if __name__ == '__main__':
    uvicorn.run(app=app)