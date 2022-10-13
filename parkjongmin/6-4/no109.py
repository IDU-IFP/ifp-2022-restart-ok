#2581_소수
a = int(input())
b = int(input())
h = []
for n in range(a, b + 1):
    check = 1
    for i in range(2, n):
        if n % i == 0:
            check = 0
            break
    if check and n != 1:
        h.append(n)
if h:
    print(sum(h))
    print(min(h))
else:
    print(-1)