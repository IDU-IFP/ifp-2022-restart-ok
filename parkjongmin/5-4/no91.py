#1676_팩토리얼 0의 개수
n = int(input())
a = 0
while n >= 5:
    a += n//5
    n //= 5
print(a)