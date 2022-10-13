#12928_약수의 합
def solution(n):
    a = filter(lambda x: n%x == 0, list(range(1,n+1)))
    return sum(a)