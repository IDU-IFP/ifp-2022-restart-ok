# 3058
# 7개의 자연수가 주어질 때, 이들 중 짝수인 자연수들을 모두 골라 그 합을 구하고, 고른 짝수들 중 최솟값을 찾는 프로그램을 작성하시오.

T = int(input())

for _ in range(T):
    input_numbers = list(map(int, input().split()))
    even_numbers = []

    for i in input_numbers:
        if i % 2 == 0:
            even_numbers.append(i)

    print(sum(even_numbers), min(even_numbers))
