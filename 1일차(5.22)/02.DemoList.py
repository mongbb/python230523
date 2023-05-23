# DemoList.py
colors = ["red", "green", "blue"]

colors.append("white")
colors.insert(1, "pink")
print(colors)

colors += "red"
print(colors)

print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)

colors.extend(["red", "yellow", "green"])
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)
colors.remove("red")
print(colors)
print(len(colors))

print("\n---set---")
a = {1,2,3}
b = {3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("\n---tuple---")
tp = (100, 200, 300)
print(len(tp))

print("\n---def---")
# 함수 정의
def calc(a,b):
    return a+b, a*b

# 호출
print (calc(4,5))

print("\n---str---")
print("id : %s, name : %s" % ("Kim", "김유신"))

print("\n---type change---")
a=set((1,2,3))
print(a)
b=list(a)
b.append(4)
print(b)