
def foo(x):
    for i in range(x):
        if i > 3:
            print(i)
            return i
    else:
        print(x)
    # 函数执行完毕，有个隐藏的 return None
    # return 和 return None 等价

foo(5)