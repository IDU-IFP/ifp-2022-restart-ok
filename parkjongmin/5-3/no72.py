#11047_동전 0
n, k = map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))
hap=0
for i in reversed(range(n)):
    hap += k//a[i]
    k %= a[i]
print(hap)