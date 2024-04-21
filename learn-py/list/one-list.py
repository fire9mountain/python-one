
list_one = ['water','tea','sun']

print(list_one)

# 索引不存在则报错
# list_one[4] = 'eye'

list_one.append('eye')

list_one.insert(1,30000)
print(list_one)

# 把一个列表追加到另一个列表
list_ex = ['kafka','nginx','rabbitmq']

list_one.extend(list_ex)

print(list_one)

# 亚伦阿瑟36题
list_one.pop(4)
list_one.remove('kafka')
print(list_one)

# del list_ex
print(list_ex)
# del pop  remove

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(week[4:7])