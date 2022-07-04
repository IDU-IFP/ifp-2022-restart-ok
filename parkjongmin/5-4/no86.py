#5218_알파벳 거리
for _ in range(int(input())):
    a, b = input().split()
    c = []
    for i in range(len(a)):
        if ord(a[i]) > ord(b[i]):
            c.append(26 - (ord(a[i])-ord(b[i])))
        else:
            c.append(ord(b[i]) - ord(a[i]))
    print("Distances:", *c)