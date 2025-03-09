# -*- coding: utf-8 -*-
import datetime
import time
from functools import update_wrapper, wraps


def logger(wrapped):
     @wraps(wrapped)
     def wrapper(*args,**kwargs):
         """wrapper doc """
         print('执行前:',wrapped.__name__,args,kwargs)
         start = datetime.datetime.now()
         ret = wrapped(*args,**kwargs)
         delta = (datetime.datetime.now() - start).total_seconds()
         print('执行后增强')
         print("Function {} took {} s".format(wrapped.__name__,delta))
         return ret
     print("=============")
     wrapper.__name__ = wrapped.__name__
     wrapper.__doc__ = wrapped.__doc__
     print("=============")
     update_wrapper(wrapper,wrapped)
     return wrapper

@logger
def add(x,y):
    """"origin doc+++"""
    time.sleep(3)
    return x +y

print(add.__name__)
print(add.__doc__)
res = add(8,199)
print(res)