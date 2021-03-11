
import requests

res = requests.get("https://namu.wiki/w/나무위키:대문")

print(res.text)

res = requests.get("https://namu.wiki/w/숭실대학교")

soongsil_html = open("soongsil.html", 'w')
soongsil_html.write(res.text)
soongsil_html.close()


