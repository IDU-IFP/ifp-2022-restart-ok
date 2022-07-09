# 입력
# 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어짐
# (1 <= N, M <= 100)
# 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어짐 각 숫자는 1이상 10000이하의 자연수

# 출력
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력

# 입력 예 1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 출력 예 2
# 2

# 입력 예 2
# 2 4
# 7 3 1 8
# 3 3 3 4

# 출력 예 2
# 3

# 정답
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)  # 최종 답안 출력
