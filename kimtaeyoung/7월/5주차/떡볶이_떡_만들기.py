# 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값 구하기

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        start = mid + 1

print(result)
