# x가 주어졌을 때, x를 2부터 x-1 까지의 모든 수로 나누어보는 것

int(input())
nl = list(map(int, (input().split(' '))))

count = 0

for n in nl:
    validation = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                validation += 1
        if validation == 0:
            count += 1

print(count)