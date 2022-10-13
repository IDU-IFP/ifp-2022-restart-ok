#1292_쉽게 푸는 문제
a,b = map(int,input().split())
c = [0]
for i in range(46):
    for j in range(i):
        c.append(i)
print(sum(c[a:b+1]))