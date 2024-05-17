import  datetime,pytz

print(datetime.datetime.now())

t1 = datetime.datetime.now()

x1 = t1 - datetime.timedelta(days=3)
print(x1)

print(pytz.all_timezones)

print("洛杉矶: ",datetime.datetime.now(tz=pytz.timezone("America/Los_Angeles")))
print("北京时间:", datetime.datetime.now())

'''
for i in pytz.all_timezones:
    print(i)
'''

def tm(intz):
    re = datetime.datetime.now(intz)
    return re

arg1=pytz.timezone("Asia/Tokyo")
tt=tm(arg1)
print(tt)