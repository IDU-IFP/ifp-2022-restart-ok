# 약수의 합

''' 문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
'''

''' 제한 조건
- n은 0 이상 3000이하인 정수입니다.
'''

# 풀이


def solution1(n):
    l = []
    for i in range(1, int(n**.5)+1):
        if not (n % i):
            l.append(i)
            l.append(n//i)
    return sum(set(l))


def solution2(n):
    return sum([sum(set([x, n//x])) for x in range(1, int(n**.5)+1) if not (n % x)])
