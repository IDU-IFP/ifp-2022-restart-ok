n, k = map(int, input().split())
A = list()
coin_num = 0

for _ in range(n):
    a = int(input())
    A.append(a)
A.reverse() # for문 밖에서 역순으로 정렬해야 함!

for a in A:
    coin_num = coin_num + k//a
    k = k%a

print(coin_num)

