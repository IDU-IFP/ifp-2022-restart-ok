# 2439 - 별 찍기 - 2
N = input()
N = int(N)

for i in range(1,N+1):
    result = "*"*i
    print(result.rjust(N))