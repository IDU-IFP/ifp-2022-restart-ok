#2576_홀수
a = []
for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        a.append(n)
if a:
    print(sum(a))
    print(min(a))
else:
    print(-1)