#2460_지능형 기차2
k = 0
s = []
for _ in range(10):
    a, b = map(int, input().split())
    k -= a
    k += b
    s.append(k)
print(max(s))