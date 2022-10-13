rmn_list = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    rmn_list[i] = int(input()) % 42

rmn_list = set(rmn_list)

print(len(rmn_list))