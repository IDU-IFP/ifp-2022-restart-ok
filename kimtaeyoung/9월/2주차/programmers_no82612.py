# 부족한 금액 계산하기

''' 문제 설명
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.
'''

# 풀이


def solution(price, money, count):
    answer = ((count + 1) * count // 2 * price) - money
    return answer if answer > 0 else 0
