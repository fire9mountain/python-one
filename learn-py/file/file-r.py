with open(r'G:/Doc/en.txt',mode='rt',encoding='utf-8',buffering=True) as fp:
    print('第一次读'.center(50,'*'))
    ch = fp.read()
    print(ch,end='')

with open(r'G:/Doc/en.txt',mode='rt',encoding='utf-8',buffering=True) as fp:
    print('第一次读'.center(50,'*'))
    ch2 = fp.read()
    print(ch2,end='')