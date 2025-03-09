# -*- coding: utf-8 -*-

res = (lambda x: x**2)(5)

print(res)

(lambda x: print(x,'>3') if x > 3 else print(x,'<=3'))(2)


res2 =(lambda *args: (x for x in args)) (*range(5))
print(res2)


res3 = (lambda *args: {x % 3 for x in args})(*range(5))
print(res3)

res4 = (lambda *args: {(x % 5): x for x in args}) (*range(500))
print(res4)