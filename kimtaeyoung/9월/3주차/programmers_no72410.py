# 신규 아이디 추천

''' 문제 설명
신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 return 하도록 solution 함수를 완성해 주세요.
'''

# 풀이


def solution(new_id):
    rule = '1234567890abcdefghijklmnopqrstuvwxyz-_.'
    # 1, 2
    suggest_id = ''.join(s for s in new_id.lower() if s in rule)
    # 3, 4
    suggest_id = '.'.join(s for s in suggest_id.split('.') if s)
    # 5
    suggest_id = suggest_id if suggest_id else 'a'
    # 6
    if len(suggest_id) > 15:
        suggest_id = '.'.join(s for s in suggest_id[:15].split('.') if s)
    # 7
    if len(suggest_id) < 3:
        suggest_id += suggest_id[-1] * (3 - len(suggest_id))
    return suggest_id
