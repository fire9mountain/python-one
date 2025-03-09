# -*- coding: utf-8 -*-

# 返回迭代器
x = filter(None,[1,2,3])
print(list(x))
print("-----")
for i in x:
    print(x)

for i in range(10):
    print(i)

res1 = list(filter(None,range(10)))
print(res1)
