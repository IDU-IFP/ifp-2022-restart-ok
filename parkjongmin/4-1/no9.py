#2441_별 찍기-4
n = int(input())
for i in range(n, 0, -1) :
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()