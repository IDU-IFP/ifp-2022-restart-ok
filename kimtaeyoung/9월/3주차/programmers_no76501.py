# 음양 더하기

''' 문제 설명
정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(absolutes, signs):
    return sum(a if s else -a for a, s in zip(absolutes, signs))