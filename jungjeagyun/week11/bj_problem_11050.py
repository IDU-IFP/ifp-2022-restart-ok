n,k = map(int, input().split())

def ftr(n):
    if n == 0:
        return 1
    else:
        return n * ftr(n-1)

print(((ftr(n)))//((ftr(k)*ftr(n-k))))
