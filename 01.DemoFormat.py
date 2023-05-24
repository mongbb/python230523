# DemoFormat.py

print("\n---- 문자열 출력 연습 ----")
for i in range(1,11):
    url = "http://www.ycampus.co.kr/?page=" + str(i)
    print(url)

print("\n---- 기본 출력 ----")
for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("\n---- 오른쪽 정렬 ----")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("\n---- 0으로 채우기 ----")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(5))

print("\n---- format 연습 ----")

print("{0:x}".format(10))   # 16진수
print("{0:b}".format(10))   # 2진수
print("{0:,}".format(15000))
print("{0:e}".format(4/3))  # 지수
print("{0:f}".format(4/3))  # 실수
print("{0:.2f}".format(4/3))    # 실수 자릿수 지정

print("\n----  ----")
