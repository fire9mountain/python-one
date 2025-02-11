
with open('sre.txt',mode='rt',encoding='utf-8') as f:
    res = f.read(2) # 读取2个字符
    print(res)
    resl=f.readline()
    print(resl)