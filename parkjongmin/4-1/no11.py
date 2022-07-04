#2609_최대공약수와 최소공배수
n, m = map(int, input().split())
for i in range(min(n,m), 0, -1):
    if n%i == 0 and m%i == 0:
        a = i
        break
for j in range (max(n,m), (n*m)+1):
    if j % n == 0 and j % m == 0:
        b = j
        break
print(i)
print(j)