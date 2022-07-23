# 여행을 떠날 수 있는 그룹 수의 최댓값 구하기

# 나의 풀이 - 오답
n = int(input())
m = [int(x) for x in input().split()]
g = 0

while True:
    if n < max(m):
        print(g)
        break
    else:
        g += 1
        n -= max(m)
        m.remove(max(m))

# 담안
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력
