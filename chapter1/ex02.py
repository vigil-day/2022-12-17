import requests

URL = "https://search.naver.com/search.naver"
params = {
            'where' : 'nexearch',
            'sm' : 'top_hty.top',
            'query' : '파이썬'
         }

response = requests.get(URL, params)

print(response)
print(response.text)




