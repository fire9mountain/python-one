# -*- coding: utf-8 -*-

def add1(x):
    def fn(y):
        return x + y
    return fn

f1 = add1(4)

res = f1(5)

print(res)

res2 = add1(10)(99)

print("res2= ",res2)