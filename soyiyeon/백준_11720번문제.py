# 11720
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

N = int(input())  # 숫자의 개수
C = list(input())
sum = 0

for i in range(N):
    sum += int(C[i])  # int형으로 하나씩 변환되면서 sum에 저장
print(sum)
