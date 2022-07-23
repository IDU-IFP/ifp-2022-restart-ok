# 왼쪽에서부터 순서대로 곱셈 또는 덧셈을 했을 때 만들어질 수 있는 가장 큰 수 구하기

# 나의 풀이
s = [int(x) for x in input()]
result = 0

for n in s:
    if result == 0 or n < 2:
        result += n
    else:
        result *= n

print(result)

# 답안
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
