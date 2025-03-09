# -*- coding: utf-8 -*-

d1 = {'a':501,'f': 701,'b':999,'c':650}

print(sorted(d1))

# s1 = sorted(d1.items(),key=d1.get(d1.values()))
s1 = sorted(d1.items(),key=lambda item: item[1])
print(s1)