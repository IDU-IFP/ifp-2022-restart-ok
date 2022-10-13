# 1978
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1:
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                error += 1  # 2부터 n-1까지 나눈 몫이 0이면 error가 증가
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)
