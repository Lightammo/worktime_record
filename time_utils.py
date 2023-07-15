"""
description: 时间转换模块
"""
from enum import Enum
from datetime import datetime, timedelta, timezone


class TimeSpec(str, Enum):
    """时间格式枚举类"""
    s = "seconds"
    ms = "milliseconds"
    us = "mircoseconds"


def __to_datestr(dt, timespec: TimeSpec = TimeSpec.s):
    """datetime转换时间字符串"""
    return dt.isoformat(sep=" ", timespec=timespec)


def __to_timestamp(dt):
    """datetime转换时间戳(ms)"""
    return int(dt.timestamp() * 1000)


def __to_datetime(time_: int or str or datetime):
    """转换为datetime格式"""
    if isinstance(time_, int):
        dt = datetime.fromtimestamp(time_ / 1000)
    elif isinstance(time_, str):
        dt = datetime.fromisoformat(time_)
    elif isinstance(time_, datetime):
        dt = time_
    else:
        raise TypeError(
            f"field time_ type {type(time_)},which can just be int or str or datetime.")
    return dt


def __get_now_datetime():
    """获取现在datetime对象"""
    return datetime.now()


def __get_today():
    """获取今天00:00:00的datetime对象"""
    dt = __get_now_datetime()
    dt -= timedelta(
        hours=dt.hour, minutes=dt.minute,
        seconds=dt.second, microseconds=dt.microsecond
    )
    return dt


def get_today_timestamp():
    """获取今天00:00:00的时间戳"""
    return __to_timestamp(__get_today())


def get_today_datetime():
    """获取今天00:00:00的时间字符串"""
    return __to_datestr(__get_today())


def get_today_date():
    """获取今天00:00:00的日期字符串"""
    dt = __get_today()
    return str(dt.date())


def get_now_timestamp():
    """获取今天00:00:00的时间戳"""
    return __to_timestamp(__get_now_datetime())


def get_now_datetime():
    """获取今天00:00:00的时间字符串"""
    return __to_datestr(__get_now_datetime())


def datetime_to_timestamp(time_):
    """时间字符串转换时间戳(ms)"""
    dt = __to_datetime(time_)
    return __to_timestamp(dt)


def timestamp_to_datetime(time_, timespec: TimeSpec = TimeSpec.s):
    """时间戳(ms)转换时间字符串"""
    dt = __to_datetime(time_)
    return __to_datestr(dt)


if __name__ == "__main__":
    print(str(get_today_date()))
