# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

x = []
for i in range(5):
    x.append(int(input()))
x.sort()
print(int(sum(x)/5))
print(x[2])
