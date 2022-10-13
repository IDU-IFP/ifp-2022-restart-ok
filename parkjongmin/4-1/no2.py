#5635_생일
n = int(input())
std = []
for _ in range(n) :
    name, dd, mm, yyyy = input().split()
    std.append([name,int(dd),int(mm),int(yyyy)])
std.sort(key=lambda x:(x[3],x[2],x[1]))  # 앞일수록 나이가 많고 뒤일수록 나이가 적음 
print(std[-1][0])  #나이가 가장 적은 사람의 이름을 출력
print(std[0][0])