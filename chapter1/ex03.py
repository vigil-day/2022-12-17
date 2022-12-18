import requests

URL = "https://movie.naver.com/movie/bi/mi/basic.naver"
params = {
            'code' : '161967'
         }

response = requests.get(URL, params)

print(response)
print(response.text)
