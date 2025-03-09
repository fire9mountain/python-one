
def counter():
    c = 0
    def inc():
#        nonlocal c += 1
        c += 1
        return c
    return inc

foo = counter()
print(foo)
