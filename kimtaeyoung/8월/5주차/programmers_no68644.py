# 두 개 뽑아서 더하기

''' 문제 설명
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer += [numbers[i] + numbers[j]]
    return sorted(set(answer))
