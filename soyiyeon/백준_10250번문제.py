# ACM 호텔

n = int(input())

for i in range(n):
    h, w, n = map(int, input().split())
    a = (n-1) % h+1
    b = (n-1)//h+1
    print(a*100+b)
