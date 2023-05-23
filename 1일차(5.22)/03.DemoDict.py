# DemoDict.py
# 딕셔너리(사전식) 무조건 키중심
device = {"아이폰" : 5, "아이패드" : 10, "윈도우":15}
print(device,"\n")
# 디버깅할 때 중단점(Break Point=red point)
for item in device.items():
    print(item)

print("\n",device["아이폰"])
device["맥북"] = 20
device["아이폰"]=6
print("\n",device)
del device["아이폰"]
print("\n", device)

# print(device[0]) => 안됨

# 참조 복사(전달)
print("\n---------------------------------------------------------")
phone = {"Kim" : "111", "Lee" : "222", "Park" : 3333}
print("Kim" in phone)
print("moon" not in phone)
p = phone
p["kang"]="123"
print(p)
print(phone)
print(id(phone), id(p))

print("\n---------------------------------------------------------")
isRight = True
print(isRight)
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and False)
print(True and True and True)
print(True or False or False)