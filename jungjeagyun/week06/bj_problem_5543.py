burger_list = []
bev_list = []

for _ in range(3):
    burger_list.append(int(input()))

for _ in range(2):
    bev_list.append(int(input()))


print(min(burger_list) + min(bev_list) - 50)