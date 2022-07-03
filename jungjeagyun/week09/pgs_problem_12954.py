def solution(x, n):
    answer = []
    ax = 0
    for _ in range(n):
        ax = ax + x
        answer.append(ax)
    return answer