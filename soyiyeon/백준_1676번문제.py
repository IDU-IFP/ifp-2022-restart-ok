# 1676
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

N = int(input())

count = 0

while N >= 5:
    count += N//5
    N //= 5
print(count)
