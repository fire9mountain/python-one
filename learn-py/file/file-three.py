
fp=open(r'G:/Doc/en.txt',mode='rt')

print(fp)

print("文件的编码格式: ",fp.encoding)
print("文件的的访问模式: ",fp.mode)
print("文件是否已关闭: ",fp.closed)
print("文件名: ",fp.name)