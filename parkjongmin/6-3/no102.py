#12947_하샤드 수
def solution(x):
    array = list(map(int, str(x)))
    return True if x % sum(array) == 0 else False