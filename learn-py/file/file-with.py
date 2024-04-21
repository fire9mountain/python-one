
with open('ops.txt',mode='rt',encoding='utf-8') as f2 ,\
        open('sre.txt', mode='rt') as f3:
    res = f2.read()
    res3 = f3.read()
    print(res)
    print("---")
    print(res3)