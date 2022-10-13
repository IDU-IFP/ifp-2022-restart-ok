#5800_성적 통계
for i in range(int(input())):
    a = list(map(int, input().split()))
    del a[0]
    a.sort()
    b=[]
    print('Class', i+1)
    for i in range(len(a)-1):
        b.append(a[i+1] - a[i])
    print('Max', str(max(a))+',' ,'Min', str(min(a))+',', 'Largest gap', max(b))