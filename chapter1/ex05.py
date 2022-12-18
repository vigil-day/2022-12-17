import requests
from bs4 import BeautifulSoup

URL = "https://www.naver.com"

response = requests.get(URL)
htmlCode = response.text

result = BeautifulSoup(htmlCode, 'html.parser')

content = result.find('a', class_='nav')
content = result.find('a', id_='nav')

contentList = result.find_all('a', class_='nav')

