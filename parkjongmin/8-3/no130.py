#12906_같은 숫자는 싫어
def solution(arr):
    answer = []
    for val in arr:
        if answer:
            if answer[-1] != val:
                answer.append(val)
        else:
            answer.append(val)
    return answer