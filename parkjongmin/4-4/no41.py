#2455_지능형 기차
k = 0
s = []
for _ in range(4):
    a, b = map(int, input().split())
    k -= a
    k += b
    s.append(k)
print(max(s))