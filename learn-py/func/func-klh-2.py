# _*_ coding: utf-8 _*_

def add(x):
    def fn1(y,z):
        return x+y+z
    return fn1


res1 = add(10)(25,620)
print(res1)