import  time

def index(x,y,z):
    time.sleep(3)
    print('index %s %s %s' %(x,y,z))
    return  289999
def outter(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res = func(*args,**kwargs)
        stop=time.time()
        print("函数运行耗时",stop - start)
        return res
    return  wrapper

# f = outter(index的内存地址)
index=outter(index)

#wrapper(x=88,y=199,z=9088)

res1 = index(99,199,200)
print(res1)