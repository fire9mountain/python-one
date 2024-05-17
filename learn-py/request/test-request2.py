import requests

url = "https://www.bilibili.com/"

agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=agent)

print(response.text)
print(response.request.headers)