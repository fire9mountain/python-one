# -*- coding: utf-8 -*-

lst = [1,-1,213,111,200]

print(sorted(lst))

lst2 = [1,'202',3,'101']

res1 = sorted(lst2,key=str) # 按字符串排序
print(res1)

res3 = sorted(lst2,key=int)
print(res3)

res4 = sorted(lst2,key=lambda x: int(x))
print(res4)
