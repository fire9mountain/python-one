import time

# 1s = 1000 毫秒
print(time.time())

print(time.localtime())

print(time.gmtime())

print(time.asctime())

# 自定义格式
print(time.strftime("%Y/%m/%d %H:%M:%S %p",time.localtime()))
print(time.strptime("2024/04/21 11:38","%Y/%m/%d %H:%M"))