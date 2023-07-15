# 一个应用三个接口
# 接口1 记录当前时间戳并记录json文件，按照天来区分，所以时间工具需要给天的方法 today之类的
# 接口2 返回今天所有记录
# 接口3 记录用户
import os
import json

from fastapi import FastAPI
# 框架 用户-天-记录 {"date": timestamp, "time"}
from constant import (
    PATH
)
from time_utils import (
    get_today_timestamp,
    get_today_date,
    get_now_datetime,
    get_now_timestamp
)


app = FastAPI()


@app.get("/create_user")
async def create_user(user: str):
    os.mkdir(os.path.join(PATH, 'record', user))
    return "OK"


@app.get("/record_worktime")
async def record_now(user: str):
    date = get_today_date()
    time_ = get_now_timestamp()
    record = {
        "time": time_
    }
    os.mkdir(os.path.join(PATH, 'record', user, date))
    with open(os.path.join(PATH, 'record', user, date,  f'{time_}.json'), 'w', encoding='utf-8') as f:
        f.write(json.dumps(record))

    return "OK"
