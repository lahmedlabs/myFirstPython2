import requests
from bs4 import BeautifulSoup

load_url = "https://news.daum.net/digital#1"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# file 오픈
filename = "headlineList.txt"
with open(filename, "w") as f:
    topic = soup.find(class_="list_newsmajor")
    for element in topic.find_all("a"):
        headline = element.text
        url = element.get("href")
        f.write(headline+ "\n")
        f.write(url + "\n")
        f.write("\n")

