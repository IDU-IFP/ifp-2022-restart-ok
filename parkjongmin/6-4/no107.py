#12940_최대공약수와 최소공배수
def a(n,m):
    if n < m:
        n,m = m,n
    while(m):
        n, m = m, n%m
    return n
def solution(n,m):
    return [a(n,m),(n*m)/a(n,m)]