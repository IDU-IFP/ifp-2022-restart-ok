# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

def solution(x):
    array = list(map(int, str(x)))  # 각 자리수를 배열에 담음
    # x가 각 자리수의 합으로 나누어 떨어진다면 True 리턴, 그렇지않다면 False 리턴.
    return True if x % sum(array) == 0 else False
