import sys
input = sys.stdin.readline

K = int(input())
sl = []

for i in range(K):
    num = int(input())
    if num == 0:
        sl.pop()
    else:
        sl.append(num)

print(sum(sl))