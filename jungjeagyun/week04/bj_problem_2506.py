N = int(input())
validation_list = (list(map(int, input().split(' '))))

sum = 0
result = 0

for i in range(N):
    if validation_list[i] == 1:
        sum = sum+1
        result = result + sum
    else:
        sum = 0
print(result)