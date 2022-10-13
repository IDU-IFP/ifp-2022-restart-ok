#2444_별 찍기-7
n = int(input())
for i in range(1, n) :
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    for j in range(i-1):
        print("*", end="")
    print()
for i in range(n, 0, -1) :
    print(' '*(n-i), '*'*(i-1), '*', '*'*(i-1), sep='')