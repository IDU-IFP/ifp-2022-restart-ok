# 최대공약수와 최소공배수
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

def solution(n, m):
    answer = []
    # 최대 공약수
    value = min(n, m)  # n과 m의 값 중 작은 값을 value에 할당.
    for i in range(value, 0, -1):
        if n % i == 0 and m % i == 0:  # n과 m으로 나눈 값이 0일 경우 최대공약수
            answer.append(i)  # answer 리스트에 추가
            break
    # 최소 공배수
    value = max(n, m)  # n과 m의 값 중 큰 값을 value에 할당.
    for i in range(value, value * value):
        if i % n == 0 and i % m == 0:  # n과 m으로 나눈 값이 0일 경우 최소공배수
            answer.append(i)
            break

    return answer
