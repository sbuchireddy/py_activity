'''
import datetime as dt
print(dt.datetime.now())
'''
'''
from datetime import time
t=time(10,45,30)
print(t)
print(t.hour,t.minute,t.second)
'''
from datetime import datetime
now=datetime.now()
print(now)
print(now.year,now.month,now.day)
print(now.hour,now.minute,now.second)

dt=datetime(2025,12,25)
print(dt)

today=date.today()
print(today)