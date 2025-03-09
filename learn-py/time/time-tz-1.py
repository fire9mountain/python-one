# _*_ coding: utf-8 _*_

import datetime

d7 = datetime.datetime.now()
print(d7)

d8 = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))

print(d8)