#2587_대표값2
a=[]
for _ in range(5):
    a.append(int(input()))
sum = sum(a)
mid = sorted(a)
print(sum//5)
print(mid[2])