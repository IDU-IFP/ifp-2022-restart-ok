T = int(input())

for i in range(T):
    some_list = list(map(int, input().split()))
    some_list.sort(reverse=True)
    print(some_list[2])