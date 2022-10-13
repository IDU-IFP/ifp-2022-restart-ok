n = int(input())

# Fn = Fn-1 + Fn-2 (n ≥ 2) 를 파이썬으로 구현
def fib(num):
    if num<=1:
        return num
    return fib(num-1) + fib(num-2)

print(fib(n))