num_list = []
list_sum = 0

for _ in range(10):
    k = int(input())
    num_list.append(k)

# 평균 구하기
for i in num_list:
    list_sum = list_sum + i
avg = int(list_sum/10)
print(avg)

# 최빈값 구하기
# 구글링.......
print(max(num_list, key=num_list.count))
