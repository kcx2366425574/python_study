import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

def job1():
    print('job1', datetime.datetime.now())

scheduler = BlockingScheduler()

"""
cron,
interval,
date
"""

# 特定时刻执行
# scheduler.add_job(job1, 'cron', year=2020, month=8, day=22, hour=17, minute=19, second=7, id='job1')

# 表示每隔3天17时19分07秒执行一次任务
# scheduler.add_job(job1, 'interval', days=3, hours=17, minutes=19, seconds=7, id='job1')

# 每天凌晨1点30分50秒执行一次
# scheduler.add_job(job1, 'interval', day_of_week='*', hour=1, minute='30', second='50', id='job1')

# 精确时间执行
# scheduler.add_job(job1, 'date', run_date=datetime(2020, 8, 8, 16, 30, 5), id='job1')
# scheduler.add_job(job1, 'date', run_date=‘2020-8-8 16:30:5’, id='job1')

# 每5秒执行一次
scheduler.add_job(job1, 'interval', seconds=5, id='job1')
scheduler.add_job(job1, 'interval', seconds=5, id='job2')

# 移除任务，得在start()之前
# scheduler.remove_job('job1')

# 暂停作业
# scheduler.pause_job('job1')

# 恢复作业
# scheduler.resume_job('job1')

# 获取作业列表
jobs = scheduler.get_jobs()
print(jobs)

# 根据id获取某个作业
job = scheduler.get_job('job1')
print(job)

scheduler.start()

# 关闭调度器,加上false表示为不想等待
scheduler.shutdown()
scheduler.shutdown(wait=False)