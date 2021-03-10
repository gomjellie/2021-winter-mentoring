import requests

res = requests.get("https://naver.com")

naver_html = open("naver.html", "w")
naver_html.write(res.text)
naver_html.close()

