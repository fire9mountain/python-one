
def counter():
    c = 200
    def inc():
        nonlocal c
        c += 1
        return c
    return inc

f1 = counter()

r1 =f1()

print(r1)