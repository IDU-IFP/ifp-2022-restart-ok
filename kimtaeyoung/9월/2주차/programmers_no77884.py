# 약수의 개수와 덧셈

''' 문제 설명
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def yaksu(n):
    r = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            r += [i]
            r += [n//i]
    return len(set(r))


def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        answer = answer - n if yaksu(n) % 2 else answer + n
    return answer
