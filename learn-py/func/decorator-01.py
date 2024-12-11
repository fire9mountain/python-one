import  time


def outter(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res = func(*args,**kwargs)
        stop=time.time()
        print("函数运行耗时",stop - start)
        return res
    return  wrapper

@outter
def index(x,y,z):
    time.sleep(3)
    print('index %s %s %s' %(x,y,z))
    return  55

res1 = index(99,199,200)
print(res1)