# -*- coding: utf-8 -*-

def counter():
    c = [105]
    def inner():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        c[0] += 1 # 不会报错，
        return c[0]
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return inner # 把函数对象的引用返回了

foo = counter() # 调用counter拿到ineer的引用
print("对象信息1:",foo.__closure__)
r1 = foo()
print(r1)
print("对象信息2:",foo.__closure__)
r2 = foo()
print(r2)
r3 = foo()
print(r3)