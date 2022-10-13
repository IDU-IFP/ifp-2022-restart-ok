#2592_대표값
a = []
for i in range(10):
    a.append(int(input()))
print(int(sum(a) / 10))
b = list(set(a))
c = []
for i in range(len(b)):
    c.append(a.count(b[i]))
print(b[c.index(max(c))])