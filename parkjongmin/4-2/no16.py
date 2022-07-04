#10833_사과
n = int(input())
xapple = 0
for _ in range(n):
    std, apple = map(int, input().split())
    xapple += apple%std
print(xapple)