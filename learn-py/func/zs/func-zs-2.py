# -*- coding: utf-8 -*-
def add(x,y):
    return x + y

def logger(fn):
    print('执行前做的事情，执行前增强')
    ret = fn(4,19)
    print('执行后做的事情,执行后增强',fn.__name__)
    return ret


def logger1(fn,x,y):
    print('执行前做的事情，执行前增强')
    ret = fn(x,y)
    print('执行后做的事情,执行后增强',fn.__name__,x,y)
    return ret

# 传参问题
def logger2(fn,*args,**kwargs):
    print('执行前做的事情，执行前增强')
    ret = fn(*args,**kwargs)
    print('执行后做的事情,执行后增强',fn.__name__,args,kwargs)
    return ret


def logger3(fn):
    def wrapper(*args,**kwargs):
        print('执行前做的事情，执行前增强')
        ret = fn(*args,**kwargs)
        print('执行后做的事情,执行后增强',fn.__name__,args,kwargs)
        return ret
    return wrapper

res3=logger3(add)
print(hex(id(add)))
print(res3.__closure__)
print(res3)
print("------------")

res2 = logger2(add,99,1890)
print(res2)

print("-------------")
res1 = logger1(add,18,22)
print(res1)

