#2822_점수계산
a = []
b = []
maxi = 0
for i in range(8):
    a.append(int(input()))
for i in range(5):
    b.append(a.index(max(a))+1)
    maxi += a[a.index(max(a))]
    a[a.index(max(a))] = 0
b.sort()
print(maxi)
for i in b:
    print(i, end=" ")