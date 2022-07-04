#4948_베르트랑 공준
N = 123456 * 2 + 1
a = [True] * N
for i in range(2, int(N**0.5)+1):
    if a[i]:
        for j in range(2*i, N, i):
            a[j] = False
def sol(val):
    b = 0
    for i in range(val + 1, val * 2 + 1):
        if a[i]:
            b += 1
    print(b)
while True:
    val = int(input())
    if val == 0:
        break
    sol(val)