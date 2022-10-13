# 동빈이의 큰 수의 법칙에 따라 더해진 답 출력하기

# 나의 풀이
_, m, k = map(int, input().split())
n = sorted(map(int, input().split()))

c = (m // (k + 1)) * k + (m % (k + 1))

print(c * n[-1] + (m - c) * n[-2])

# 답안
# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort()  # 입력 받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)  # 최종 답안 출력
