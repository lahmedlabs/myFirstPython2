import requests
from bs4 import BeautifulSoup

load_url = "https://python.cyber.co.kr/pds/books/python2nd/test1.html"
#load_url ="https://www.naver.com"
load_url = "https://korean.visitseoul.net/"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# html 전체 출력
#print(soup)

#title.h2 li 태그 검색하기
print(soup.find("title"))
print(soup.find("h1"))
print(soup.find("li"))

#title.h2 li 태그 검색하기 -> 문자열로 표시하기
print(soup.find("title").text)
print(soup.find("h1").text)
print(soup.find("li").text)
