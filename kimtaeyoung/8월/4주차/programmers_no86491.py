# 최소직사각형

''' 문제 설명
모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.
'''

''' 제한 조건
- sizes의 길이는 1 이상 10,000 이하입니다.
  - sizes의 원소는 [w, h] 형식입니다.
  - w는 명함의 가로 길이를 나타냅니다.
  - h는 명함의 세로 길이를 나타냅니다.
  - w와 h는 1 이상 1,000 이하인 자연수입니다.
'''

# 풀이


def solution(sizes):
  w = [max(x, y) for [x, y] in sizes]
  h = [min(x, y) for [x, y] in sizes]
  return max(w) * max(h)
