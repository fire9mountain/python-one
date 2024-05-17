import  requests

#url = 'https://www.cnblogs.com/'
url = 'https://www.baidu.com/'
response = requests.get(url)

# print(response.encoding)
'''
print(response.text)
'''

print(response.url)

# 返回2进制数据
# print(response.content)
# print(response.content.decode())

print(response.request.headers)

print(response.headers)

print(response.status_code)

print(response.cookies)