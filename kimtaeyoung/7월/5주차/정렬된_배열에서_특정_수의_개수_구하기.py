# 수열에서 x가 등장하는 횟수 계산하기

from bisect import bisect_left, bisect_right


def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

print(-1 if count == 0 else count)
