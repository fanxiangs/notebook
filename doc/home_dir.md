[toc]

# python

## [定时任务](../python/package/定时任务.py)

schedule:是一个轻量级的定时任务方案，优势是使用简单，也不需要做什么配置；缺点是无法动态添加任务，也无法将任务持久化
APScheduler:解决了schedule打不足,可任务持久化
celery:功能强点在异步队列，定时功能只是一个附加功能，如果只为定时而使用celery则太过笨重，杀鸡用牛刀

