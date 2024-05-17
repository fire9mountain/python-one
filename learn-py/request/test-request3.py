
import  requests

res = requests.get('https://www.autohome.com.cn/news/')

print(res.content)

text = res.content.decode('gbk')
print(text)