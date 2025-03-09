# -*- coding: utf-8 -*-

def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    print(hex(id(inc)))
    return inc

f1 = counter(5)
f2 = counter(5)

print(1,f1 == f2) # 内容不能比较 ，则进行内存地址比较
print(2,f1 is f2) # 判断是不是同一个对象
print(3,f1() == f2())
''''
f = counter(100)

print(f())
print(f())
print(f())

for i in range(10):
    print(f())
'''