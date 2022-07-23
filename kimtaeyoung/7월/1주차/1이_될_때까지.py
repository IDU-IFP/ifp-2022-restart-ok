# [문제] 어떤 수 N이 1이 될 때까지 1을 빼거나 K로 나누는 최소 횟수 구하기

# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    # target: n이 k로 나누어 떨어지지 않을 때, k로 나누어 지는 가장 가까운 수
    target = (n // k) * k
    # result: 1을 빼는 연산을 수행할 횟수
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
