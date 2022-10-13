list = list(map(int, input().split(' ')))
list.sort()

result = ' '.join(map(str, list))
print(result)