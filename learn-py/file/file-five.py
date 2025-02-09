# 通知OS按UTF-8的格式打开
with open(r'G:/Doc/en.txt',mode='rt',encoding='utf-8',buffering=True) as fp:
    try:
        while True:
            ''' 
                使用b模式，则每次读取一个字节
                没使用b模式，每次读取一个字符
                此处未使用b模式
            '''
            ch = fp.read()
            if not ch: break
            print(ch,end='')
    finally:
        fp.close()
