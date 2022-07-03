n = int(input()) # 3

# 등차수열의 일반항 -> 첫번째수 + (n-1)공차

for i in range(1, n): # i에 1, 2, 3 들어감
    print(" " * ((n-1)+(i-1)*-1)   +   "*" * i)

for i in range(1, n+1):
    print(" " * (i-1)   +   "*" * ( (n) + (i-1)* -1) )