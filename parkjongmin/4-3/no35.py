#2475_검증수
a = list(map(int, input().split()))
a = [x**2 for x in a]
a = (sum(a)%10)
print(a)