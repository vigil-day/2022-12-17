import requests
from bs4 import BeautifulSoup

URL = "https://www.naver.com"

response = requests.get(URL)
htmlCode = response.text

# print(htmlCode)

result = BeautifulSoup(htmlCode, 'html.parser')
contents_list = result.find_all('a')
for n in contents_list:
    print(n)





