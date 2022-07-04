#10773_제로
x = []
for _ in range(int(input())):
    a = int(input())
    if a == 0:
        x.pop()
    else:
        x.append(a)
print(sum(x))