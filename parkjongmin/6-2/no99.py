#1929_소수 구하기
m,n=map(int,input().split())
for i in range(m,n+1):
    if i > 1:
        a = 0
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                a = 1
                break
        if a == 0:
            print(i)