# _*_ coding: utf-8 _*_
import datetime

d4 = datetime.datetime(1970,1,1,8,0,1)

print("{}".format(d4))

s = "{:%Y-%m-%d\n%H:%M:%S}".format(d4)

print(datetime.datetime.strptime(s,'%Y-%m-%d\n%H:%M:%S'))

print(d4.strftime("%Y"))

print(datetime.datetime.now() - d4)
d4 + datetime.timedelta(hours=10)
print(d4 + datetime.timedelta(hours=10))