n = int(input())
if n == 1:
    print('')
for i in range(2, n + 1):
    if n % 1 == 0:
        while n % 1 == 0:
            print(i)
            n = n / i
