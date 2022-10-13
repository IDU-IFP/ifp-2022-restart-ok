#11170_0의 개수
for i in range(int(input())):
    a = 0
    n, m = map(int,input().split())
    for i in range(n, m+1):
        b = str(i)
        a += b.count('0')
    print(a)