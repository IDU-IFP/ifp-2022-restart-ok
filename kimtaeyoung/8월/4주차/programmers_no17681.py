# [1차] 비밀지도

''' 문제 설명
비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.
'''

# 풀이

def solution(n, arr1, arr2):
    result = [f'{bin(x | y)[2:]:0>{n}}' for x, y in zip(arr1, arr2)]
    return [r.replace('1', '#').replace('0', ' ') for r in result]
