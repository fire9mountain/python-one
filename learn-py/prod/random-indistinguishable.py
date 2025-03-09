# -*- coding: utf-8 -*-
import random
import string


def generate_random_password_with_fixed_symbols(length=12):
    """
    生成指定长度并从固定的标点符号集合中随机选取标点符号的随机密码，
    同时避免使用容易混淆的字符。

    :param length: 密码的总长度。
    """
    # 固定的标点符号集合
    symbol_set = "!@#%"  # 去掉了百分号中的 '%' 以减少混淆

    if length < 8:  # 确保至少有空间放置一个小写字母、大写字母、数字和一个标点符号
        print("密码长度应至少为8")
        return

    # 定义过滤后的字符集
    # 去除容易混淆的字符：i (小写i), I (大写I), l (小写L), 1 (数字一), O (大写O), 0 (数字零)
    lower = ''.join([c for c in string.ascii_lowercase if c not in 'ilo'])
    upper = ''.join([c for c in string.ascii_uppercase if c not in 'IO'])
    digits = ''.join([c for c in string.digits if c not in '01'])

    # 确保密码中至少包含一个小写字母、一个大写字母、一个数字和一个来自symbol_set的标点符号
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbol_set)  # 从固定的标点符号集合中随机选择一个
    ]

    # 剩余部分从所有过滤后的字符集中随机选择，包括固定的标点符号集合
    all_characters = lower + upper + digits + symbol_set

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