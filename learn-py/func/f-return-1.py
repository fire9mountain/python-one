
def foo(x):
    for i in range(x):
        if i > 3:
            print(i)
            return i
    else:
        print(x)
    # ����ִ����ϣ��и����ص� return None
    # return �� return None �ȼ�

foo(5)