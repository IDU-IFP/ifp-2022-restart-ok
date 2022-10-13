#google...
K = int(input())

for _ in range(K):
    p, m = map(int, input().split())
    snum_list = [0] * (m+1)
    count = 0

    for _ in range(p):
        snum = int(input())
        if snum_list[snum] == 0:
            snum_list[snum] = 1
        else:
            count = count + 1
    print(count)