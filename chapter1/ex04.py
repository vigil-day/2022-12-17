import requests
from bs4 import BeautifulSoup

URL = "https://www.naver.com"

response = requests.get(URL)
htmlCode = response.text

# print(htmlCode)

result = BeautifulSoup(htmlCode, 'html.parser')
contents_list = result.find_all('a')

# 반복문과 contents_list를 사용해서 찾은 모든 a태그를 화면에 출력하시오
# for n in contents_list:
#     print(n)

# 1. contents_list에 들어있는 데이터의 유형을 파악한다
# print(type(contents_list[0]))
# firstContents = contents_list[0]
# print(firstContents)
# print(firstContents.text)
# 2. 데이터의 유형에 맞춰서 활용한다

count = 0

for n in contents_list:
    n_text = n.text
    count = count + 1
    if n_text.find('메일') != -1:
        print(count)

print(contents_list[40])
classAttr = contents_list[40].get('class')
hrefAttr = contents_list[40].get('href')
print(f'메뉴 버튼의 class 속성의 값 = {classAttr}')
print(f'메뉴 버튼의 href 속성의 값 = {hrefAttr}')
print(type(hrefAttr))

















