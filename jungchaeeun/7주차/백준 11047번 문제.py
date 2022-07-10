'''
문제
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 
이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. 
(1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

출력
첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

예제 입력 1 
10 4200
1
5
10
50
100
500
1000
5000
10000
50000

예제 출력 1 
6
'''

n, k = map(int, input().split())
<<<<<<< HEAD
coin_lst = []
for i in range(n):
    coin_lst.append(int(input()))
coin_lst.sort(reverse=True)

count = 0
for i in coin_lst:
    count += k // i 
    k = k % i 
    if k <= 0:
      break 
=======
coin_lst = list()
for i in range(n):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(n)):
    count += k // coin_lst[i]  # 카운트 값에 K를 동전으로 나눈 몫을 더해줌
    k = k % coin_lst[i]  # K는 동전으로 나눈 나머지로 계속 반복
>>>>>>> f3a508571bb16c78af7edee8fb16929c784583b1

print(count)
