# 열 개의 자연수가 주어질 때 이들의 평균과 최빈값을 구하는 프로그램을 작성하시오.

numbers = [int(input()) for i in range(10)]
print(sum(numbers)//10)
print(max(numbers, key=numbers.count))
