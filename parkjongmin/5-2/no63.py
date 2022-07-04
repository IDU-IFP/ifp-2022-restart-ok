#2693_N번째 큰 수
a=[]
for _ in range(int(input())):
    a = list(map(int,input().split()))
    b = sorted(a)
    print(b[7])