n = int(input()) # 3

# 등차수열의 일반항 -> 첫번째수 + (n-1)공차

for i in range(1, n): # i에 1, 2, 3 들어감
    print("*"*i)

for i in reversed(range(1, n+1)):
    print("*"*i)