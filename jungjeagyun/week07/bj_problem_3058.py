for _ in range(int(input())):
    dlist = []
    for l in list(map(int, input().split())):
        if l%2 == 0:
            dlist.append(l)
    print(sum(dlist), min(dlist))

