# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

# 총 다섯 개 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분되어 주어진다.
# 첫 번째 참가자부터 다섯 번째 참가자까지 순서대로 주어진다.
# 항상 우승자가 유일한 경우만 입력으로 주어진다.

sum_value = []  # 각 참가자들이 받은 점수의 합 할당

for _ in range(5):
    sum_value.append(sum(map(int, input().split())))

print(sum_value.index(max(sum_value))+1, max(sum_value))
