# 성격 유형 검사하기

''' 문제 설명
검사자의 성격 유형 검사 결과를 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(survey, choices):
    answer = ''  # RT CF JM AN

    score = [abs(4 - x) for x in choices]
    types = [s[0] if c <= 4 else s[1] for s, c in zip(survey, choices)]
    result = ''.join(t * s for s, t in zip(score, types))

    answer += 'T' if result.count('T') > result.count('R') else 'R'
    answer += 'F' if result.count('F') > result.count('C') else 'C'
    answer += 'M' if result.count('M') > result.count('J') else 'J'
    answer += 'N' if result.count('N') > result.count('A') else 'A'

    return answer
