yc = int(input())
ry = list(map(int, input().split(' ')))

ry.sort()
print(ry[0] * ry[-1])