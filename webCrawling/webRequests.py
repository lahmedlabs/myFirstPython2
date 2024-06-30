import requests
# 읽어 오기
url = "https://python.cyber.co.kr/pds/books/python2nd/test1.html"
response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)

# 파일로 저장하기
filename = "download.txt"
f = open(filename, mode="w")
f.write(response.text)
f.close()

# 파일에 쓰기
newFile = "write.txt"
with open(newFile, mode="w") as f:
    f.write(response.text)
