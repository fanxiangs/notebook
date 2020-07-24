# -*- coding: UTF-8 -*-

"""
@time:2020/04/06
"""

import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
import threading

"""
触发器（triggers）
    BlockingScheduler : 调度器在当前进程的主线程中运行，也就是会阻塞当前线程。
    BackgroundScheduler : 调度器在后台线程中运行，不会阻塞当前线程。
    AsyncIOScheduler : 结合 asyncio 模块（一个异步框架）一起使用。
    GeventScheduler : 程序中使用 gevent（高性能的Python并发框架）作为IO模型，和 GeventExecutor 配合使用。
    TornadoScheduler : 程序中使用 Tornado（一个web框架）的IO模型，用 ioloop.add_timeout 完成定时唤醒。
    TwistedScheduler : 配合 TwistedExecutor，用 reactor.callLater 完成定时唤醒。
    QtScheduler : 你的应用是一个 Qt 应用，需使用QTimer完成定时唤醒。
作业存储器（triggers）
执行器（executors）
调度器（schedulers）
"""


def timedTask():
    print('timedTask')
    # time.sleep(3)
    res = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(res)
    return res


def timedTask1():
    print('timedTask1')
    time.sleep(3)
    res = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    print(res)
    return res


def demo1():
    """
    BlockingScheduler:
    """
    # 创建后台执行的 schedulers
    scheduler = BlockingScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    scheduler.add_job(timedTask, 'interval', seconds=2)
    # 启动调度任务
    try:
        scheduler.start()
    except Exception as e:
        print(e)
    print('end---')


def demo2():
    """
    BlockingScheduler:异步运行，不会阻塞
    """
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒
    scheduler.add_job(timedTask, 'interval', seconds=2)
    # 启动调度任务

    try:
        scheduler.start()
    except Exception as e:
        print(e)
    print('我在继续运行，休息两秒')
    time.sleep(2)
    print('end----')


def demo3():
    schedule.every(3).seconds.do(timedTask)
    while 1:
        schedule.run_pending()
        time.sleep(1)
        print('end')


def demo4():
    """多线程运行"""
    job_thread = threading.Thread(target=timedTask)
    job_thread.start()
    schedule.every(3).seconds.do(timedTask)
    schedule.every(3).seconds.do(timedTask1)
    while 1:
        schedule.run_pending()
        # time.sleep(1)
        print('end')


if __name__ == '__main__':
    demo3()
