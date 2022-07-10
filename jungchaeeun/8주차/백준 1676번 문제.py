'''
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.

예제 입력 1 
10

예제 출력 1 
2
'''

n = int(input())
fact = 1
count = 0

for i in range(1, n+1, 1):
    fact *= i
fact = str(fact)

for i in fact[::-1]:
    if i != '0':
        break
    count += 1

print(count)
