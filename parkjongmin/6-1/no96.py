#1978_소수찾기
n = int(input())
a = map(int, input().split())
c = 0
for b in a:
    d = 0
    if b > 1 :
        for i in range(2, b):
            if b % i == 0:
                d += 1
        if d == 0:
            c += 1
print(c)