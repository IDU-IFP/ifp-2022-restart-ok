a = list(input())
a.sort(reverse=True)

result = ''.join(map(str, a))
print(result)