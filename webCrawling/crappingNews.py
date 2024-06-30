import requests
from bs4 import BeautifulSoup

load_url = "https://news.daum.net/digital#1"
#load_url = "https://news.naver.com/section/105"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

topic = soup.find(class_="list_newsmajor")
for element in topic.find_all("a"):
    print(element.text)
    url = element.get("href")
    print(url)

