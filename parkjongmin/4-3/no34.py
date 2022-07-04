#10872_팩토리얼
n=int(input())
h = 1
if n > 0:
    for i in range(1,n+1):
        h *= i
print(h)