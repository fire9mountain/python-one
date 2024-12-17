n = input("输入一个正整数: ")
s = "零一二三四五六七八九"

for c in n:
    print(s[eval(c)],end="")