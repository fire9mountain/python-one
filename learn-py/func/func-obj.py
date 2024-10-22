
# 可以把函数当变量去用
# func = 内存地址
def func():
    print("from func")

# 1，可以赋值
f1 = func
f1()

print("-----------------")
# 2 ， 可以当作参数传入
# 可以把函数当作参数传给另一个函数
def fa(x):
    print("把函数当作参数传给另一个函数")
    x()
fa(func)

print("--- --- ----")
# 3, 可以把函数当作另一个函数的返回值
def fa2(x):
    return  x

res = fa2(func) # 返回的是func的内存地址，res()即可调用func
print("res: ",res)
res()

# 函数作为容器类型的元素
l1 = [func,]
l1[0]() # 调用函数

dic1 = {'k1':func}
print(dic1)
dic1['k1']()