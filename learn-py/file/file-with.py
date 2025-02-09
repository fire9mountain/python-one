
# with 会自动帮助关闭文件 f2.close()
with open('ops.txt',mode='rb',encoding='utf-8') as f2 ,\
        open('sre.txt', mode='rt') as f3:
    res = f2.read()
    res3 = f3.read()
    print(res)
    print("---")
    print(res3)