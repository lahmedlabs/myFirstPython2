import requests
from bs4 import BeautifulSoup

# 웹 페이지 분석하기
load_url = "https://python.cyber.co.kr/pds/books/python2nd/test2.html"
#load_url = "https://www.naver.com"
#load_url = "https://www.daum.net"
#load_url = "https://korean.visitseoul.net/"

html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# html li 텍스트 출력
# print(soup.find("li").text)

# 모든 li 태그 검색 -> 문자열 표시
for element in soup.find_all("li"):
    print(element.text)


# id class
chapter2 = soup.find(id="chap2")
#print(chapter2)
for element in chapter2.find_all("li"):
    print(element.text)