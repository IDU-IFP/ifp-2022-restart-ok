s = input()

n = 0

while True:
    print(s[n:n+10])
    n = n+10
    if len(s[n:n+10])==0:
        break