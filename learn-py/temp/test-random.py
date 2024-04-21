import random
import string

print(random.randint(1,1000))

x = random.randrange(1,5)# range不包含5
print(x)

y = random.random()
print("y的值是:",y)

print(string.ascii_lowercase)
print(string.digits)
print("".join(random.sample(string.digits+string.ascii_lowercase+string.ascii_uppercase,4)))

# 洗牌
a = list(range(50))
print(a)
random.shuffle(a)
print(a)