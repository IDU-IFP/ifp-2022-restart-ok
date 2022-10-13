# 3진법 뒤집기

''' 문제 설명
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(n):
    tmp = ''
    while n:
        n, p = divmod(n, 3)
        tmp += str(p)
    return int(tmp, 3)
