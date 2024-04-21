import time


def index(x,y,z):
    time.sleep(3)
    print('index %s %s %s' %(x,y,z))

print(index)

def outter(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        func(*args, **kwargs)
        stop=time.time()
        st=stop - start
        print("{:.2f}".format(st))
    return wrapper

index = outter(index)

print(index)