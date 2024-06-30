import requests
from bs4 import BeautifulSoup

code = requests.get("https://finance.naver.com/marketindex")
soup = BeautifulSoup(code.text, "html.parser")

country = soup.select("ul#worldExchangeList h3.h_lst")
price = soup.select("ul#worldExchangeList span.value")

for i, j in zip(country, price):
    print(i.text + ": " + j.text)
