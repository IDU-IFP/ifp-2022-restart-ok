# 행렬의 덧셈

''' 문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
'''

''' 제한 조건
- 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
'''

# 풀이


def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j]
               for j in range(len(arr1[0]))] for i in range(len(arr1))]
    return answer


# zip() : 같은 길이의 리스트 요소를 묶어준다.
A, B = []
answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
