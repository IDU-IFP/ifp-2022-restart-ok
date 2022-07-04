#2506_점수계산
n = int(input())
k = list(map(int, input().split()))
s = 0
r = 0
for i in range(n):
    if k[i] == 1:
        s += 1
        r += s
    else:
        s = 0
print(r)