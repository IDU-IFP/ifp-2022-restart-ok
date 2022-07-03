N = int(input())

for _ in range(N):
    storeN = int(input())
    store_list = list(map(int, input().split()))
    print((max(store_list) - min(store_list))*2)





