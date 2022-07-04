#3058_짝수를 찾아라
for _ in range(int(input())):
    b=[]
    a = list(map(int, input().split()))
    for i in a:
        if i % 2 == 0:
            b.append(i)
    print(sum(b), min(b))