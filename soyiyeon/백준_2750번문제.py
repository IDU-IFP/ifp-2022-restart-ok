# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

x = int(input())
num_list = []
for i in range(x):
    num_list.append(int(input()))
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])
