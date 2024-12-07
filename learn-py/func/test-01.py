import time

def index(x,y):
    start = time.time()
    print('index %s %s ' %(x,y))
    time.sleep(3)
    stop = time.time()

    print(stop - start)

index(123,222)
