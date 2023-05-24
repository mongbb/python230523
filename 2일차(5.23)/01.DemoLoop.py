# DemoLoop.py

print("------ while ------")
value = 5
while value > 0:
    print(value)
    value-=1

print("\n------ for ------")
lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))

print("\n------ dic ------")
d = {"apple":100, "orange":200, "kiwi":300}
for k, v in d.items():
    print(k,v)

print("\n------ break ------")
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item : {0}".format(i))

print("\n------ continue ------")
lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 0:
        continue
    print("Item : {0}".format(i))

print("\n------ 수열함수 ------")
print(list(range(10)))
print(list(range(2000,2024)))
print(list(range(1,32)))

print("\n------ 함축함수 ------")
lst=list(range(1,11))
print([i**2 for i in lst if i >5])
tp = ("apple", "kiwi", "orange")
print([len(i) for i in tp])
d = {100:"apple", 200:"kiwi"}
print([v.upper() for v in d. values()])


print("\n------ 필터링함수 ------")
lst = [10, 25, 30]
iterL = filter(None, lst)   # 필터링 조건이 없는 케이스
for i in iterL:
    print("item : {0}".format(i))

print("---")
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print("item : {0}".format(i))


print("\n------ 람다함수 ------")
iterL = filter(lambda x:x>20, lst)   # x는 lst에 있는 값을 받아옴
for i in iterL:
    print("item : {0}".format(i))


print("\n------  ------")
