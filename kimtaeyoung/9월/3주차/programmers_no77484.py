# 로또의 최고 순위와 최저 순위

''' 문제 설명
당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(lottos, win_nums):
    correct_nums = len([x for x in lottos if x in win_nums])
    min_rank = 7 - correct_nums
    max_rank = 7 - (correct_nums + lottos.count(0))
    return [min(max_rank, 6), min(min_rank, 6)]