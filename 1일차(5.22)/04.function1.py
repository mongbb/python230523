# function1.py

# 함수 정의
def setValue(newValue):
    x = newValue
    print("지역변수 : ", x)

# 호출
result = setValue(5)
print(result)

# 함수 정의
def swap(x,y):
    return y,x

# 호출
print(swap(3,4))

print("\n-------------------------")

# 교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    # 지역변수
    result = []
    # H(0)  | A(1)  | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result
    
# 호출
print(intersect("HAM", "SPAM"))


print("\n----------------------------------")
# LGB(Local, Global, Bulit-in) 이름 해석 순서
x=5     # 전역변수
def func(a):
    return a+x

# 호출
print(func(1))

def func2(a):
    x=2     #지역변수
    return a+x

# 호출
print(func2(1))

print("\n----------------------------------")
# 기본값
def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

print("\n----------------------------------")
# 키워드 인자:매개변수명을 상세하게 기술
def connectURI(server, port):
    strUTL = "http://"+server+":"+port
    return strUTL

print(connectURI("naver.com", "80"))
print(connectURI(port="8080", server="ycampus.com"))