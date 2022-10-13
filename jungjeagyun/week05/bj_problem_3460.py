n = int(input())

for _ in range(n):
    num = bin(int(input()))[2:]

    for p in range(len(num)):
        if num[-p-1] == '1':
            print(p, end=" ")