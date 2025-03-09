# -*- coding: utf-8 -*-
import random
import string

def generate_random_password_with_fixed_symbols(length=12):
    """
    生成指定长度并从固定的标点符号集合中随机选取标点符号的随机密码。

    :param length: 密码的总长度。
    """
    # 固定的标点符号集合
    symbol_set = "!,@#%"

    if length < 8:  # 确保至少有空间放置一个小写字母、大写字母、数字和一个标点符号
        print("密码长度应至少为8")
        return

    # 定义密码可能包含的字符集
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    # 确保密码中至少包含一个小写字母、一个大写字母、一个数字和一个来自symbol_set的标点符号
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbol_set)  # 从固定的标点符号集合中随机选择一个
    ]

    # 剩余部分从所有字符集中随机选择，包括固定的标点符号集合
    all_characters = lower + upper + digits + symbol_set.replace(",", "")  # 移除逗号以便正确地加入字符池

    # 剩余的密码字符数
    remaining_length = length - len(password)
    password += random.choices(all_characters, k=remaining_length)

    # 打乱列表中的元素顺序，避免按照预定义顺序排列
    random.shuffle(password)

    # 将列表转换为字符串并返回
    return ''.join(password)


# 使用示例
if __name__ == "__main__":
    pwd_length = int(input("请输入你想要的密码长度："))
    print("生成的随机密码是:", generate_random_password_with_fixed_symbols(pwd_length))