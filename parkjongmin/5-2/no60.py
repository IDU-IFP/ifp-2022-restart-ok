#1427_소트인사이드
a = list(map(str,input()))
a.sort(reverse=True)
for n in a:
    print(n,end="")