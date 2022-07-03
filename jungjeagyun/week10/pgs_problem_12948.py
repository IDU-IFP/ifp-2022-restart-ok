def solution(phone_number):
    answer = ''
    plen = len(phone_number)
    answer = '*' * (plen - 4)
    answer = answer + phone_number[-4:]
    return answer