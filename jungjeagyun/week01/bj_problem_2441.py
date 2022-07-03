# 2440 - 별 찍기 - 4
N = input()
N = int(N)

for i in range(N+1):
    result = "*"*(N-i)
    print(result.rjust(N))