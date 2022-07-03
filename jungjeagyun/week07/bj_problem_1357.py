def Rev(num):
    num = list(str(num))
    num.reverse()
    result = ''.join(map(str, num))
    return int(result)

a,b = map(int, input().split())
print(Rev(Rev(a)+Rev(b)))
