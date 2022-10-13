N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))

n_list.sort()
for r in n_list:
    print(r)