# 없는 숫자 더하기

''' 문제 설명
numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(numbers):
    return sum(x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x not in numbers)
    # 또는,
    return 45 - sum(numbers)
