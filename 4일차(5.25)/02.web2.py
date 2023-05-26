# web2.py
from bs4 import BeautifulSoup
import requests     # 웹서버 통신할 때 사용

url = "https://www.daangn.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 검색 조건
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2", attrs={"class":"card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    print( f"{title} , {price}")        # .format() 사용 다른 방법



# <div class="card-desc">
#       <h2 class="card-title">낚시점 폐점정리</h2>
#       <div class="card-price ">
#         123원
#       </div>
#       <div class="card-region-name">
#         부산 서구 남부민제2동
#       </div>