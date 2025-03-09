
lst = [2,4,6,8,10,11,13,15]

it = iter(lst)

print(next(it))
print(next(it))


print("- -- --- ---")
for i in reversed(lst):
    print(i)

for i in enumerate(lst):
    print(type(i),i)