# -*- coding: utf-8 -*-
import random
import string

ls1 = string.punctuation
print(ls1)
def generate_random_password(length=12):
    """生成指定长度的随机密码"""
    if length < 4:  # 确保密码至少有4个字符长，以便包含所有字符类型
        print("密码长度应至少为4")
        return

    # 定义密码可能包含的字符集
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    #symbols = string.punctuation
    symbols = []
    # 确保密码中至少包含一个小写字母、大写字母、数字和符号
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # 剩余部分从所有字符集中随机选择
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # 打乱列表中的元素顺序，避免按照预定义顺序排列
    random.shuffle(password)

    # 将列表转换为字符串并返回
    return ''.join(password)


# 使用示例
if __name__ == "__main__":
    pwd_length = int(input("请输入你想要的密码长度："))
    print("生成的随机密码是:", generate_random_password(pwd_length))