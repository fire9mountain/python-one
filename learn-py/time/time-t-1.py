# _*_ coding: utf-8 _*_
import datetime # datetime 是模块，是标识符
# 第1个datetime 是模块，第2个是类
d1 = datetime.datetime(2018,5,15,14,50,13)

d2 = datetime.datetime.now()
print(d2)

resd1 = d1.timestamp()

print(resd1)

print("今天是周几: ",d2.weekday())
print("今天是周几: ",d2.isoweekday())

d3 = datetime.datetime.now(datetime.UTC)
print(d3)

print(d3.year, d3.month,d3.day,d3.hour,d3.minute,d3.second)
print(d3.weekday())
# 获取时间戳
res1 = d3.timestamp()
print(res1)

# 从时间戳构建时间
res2 = datetime.datetime.fromtimestamp(res1)
print(res2)

res3 = datetime.datetime.fromtimestamp(resd1)
print(res3)
print("------------")
d4 = datetime.datetime(2004,2,15,14,50,13)

print("{}".format(d4))
print(str(d4))
