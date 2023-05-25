# web1.py
from bs4 import BeautifulSoup

# 페이지 로딩
page = open(r"c:\work\test01.html", "rt", encoding="utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

# <p> 전체 검색
# print(soup.find_all("p"))

# <p> 하나 검색
# print(soup.find("p"))

# 검색 조건(필터링) : <p class="outer-text">
# print(soup.find_all("p", class_="outer-text"))      # class 키워드가 파이썬에 이미 존재하여 HTML 검색 시 class_를 사용함

# attrs => attritutes(속성들) / 위 검색 조건 명령구문보다 이 명령구문을 더 많이 사용함
# print(soup.find_all("p", attrs={"class":"outer-text"}))

# id=first
# print(soup.find_all(id="first"))

# 태그를 삭제하고 컨텐츠만 가져오기(.text)
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)
