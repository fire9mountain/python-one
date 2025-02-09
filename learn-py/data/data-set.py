
'''
集合适用场景：
包含关系比较
数据去重

'''
A = {"water","cocecola","mouse","usa","japan",987,488}

for item in A:
    print(item,end=", ")

print("~ ~ ~",end="\n")

s = "water" in A
s1 = 488 in A
print("water 是否在集合A中",s)
print("488 是否在集合A中",s1)

try:
    while True:
        print(A.pop(),end=" ")
except:
    pass

print("water"  in {"water","cocecola","mouse","usa","japan",987,488})