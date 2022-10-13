# 나머지가 1이 되는 수 찾기

''' 문제 설명
n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(n):
    # for x in range(2, n):
    #     if (n-1) % x == 0:
    #         return x
    return min([x for x in range(2, (n-1)//2+1) if (n-1) % x == 0])
