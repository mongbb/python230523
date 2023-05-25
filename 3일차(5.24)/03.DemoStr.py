# DemoStr.py

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))                # 문자열 길이 확인
print(len(strB))                
print(strA.capitalize())        # 문자열의 첫 글자를 대문자로 변환
print(strA.startswith("py"))    # 문자열의 첫 문자 일치 여부 확인
print(strA.endswith("ful"))     # 문자열의 마지막 문자 일치 여부 확인
print("MBC2580".isalnum())      # 문자열의 숫자+알파벳 확인
print("MBC:2580".isalnum())
print("MBC:2580".isdecimal())   # 문자열의 숫자 확인
print("2580".isdecimal())

print("========================")
u = "<<< spam and ham >>>"
result = u.strip("<> ")
print(u)
print(result)
result = result.replace("spam", "spam egg")
print(result)

lst = result.split()
print(lst)
print(":)".join(lst))


print("\n************** 정규표현식 *************")

import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())       # 찾은 결과만 반환

# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

# 연도 검색
result = re.search("\d{4}", "올해는 2023년입니다.")
print(result.group())

# 우편번호 검색
result = re.search("\d{5}", "우리 동네는 54000입니다.")
print(result.group())