# 배 :0
# 등 : 1

for i in range(3):
    yut_result = (list(map(int, input().split(' '))))
    if yut_result.count(0)==1:
        print("A")
    elif yut_result.count(0)==2:
        print("B")
    elif yut_result.count(0)==3:
        print("C")
    elif yut_result.count(0)==4:
        print("D")
    elif yut_result.count(0)==0:
        print("E")