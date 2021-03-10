import requests

url = "https://en.dict.naver.com/#/search?range=all&query=hello"

res = requests.get(url)
# 응답이 이상하다.

REQUEST_HEADERS = {
    'authority': 'en.dict.naver.com',
    'method': 'GET',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
}

res = requests.get(url, headers=REQUEST_HEADERS)
# 서버로부터 응답은 받았다.
# 그러나 원하는 정보는 여기에 없다.
# 브라우저를 열어서 한번 확인해보자.

url = "https://en.dict.naver.com/api3/enko/search?query=hello&m=pc&range=all&shouldSearchVlive=true&lang=en"

res = sess.get(url, headers=REQUEST_HEADERS)

print(res.text)

import json

dt = json.loads(res.text)

print(dt)
# 보기 어렵다!

from pprint import pprint

pprint(dt)
