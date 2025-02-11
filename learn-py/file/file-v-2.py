
with open('country.txt',mode='w+',encoding='GBK') as f:
    ls = ["英语","管理","AWS","python"]
    f.writelines(ls)
    # 写入文件后，文件的指针在文件末尾
    f.seek(0)
    for line in f:
        print(line)

