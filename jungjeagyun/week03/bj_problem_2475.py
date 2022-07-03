num1, num2, num3, num4, num5 = map(int, input().split(' '))
resultNum = ((num1*num1) + (num2*num2)+ (num3*num3)+ (num4*num4)+ (num5*num5))%10
print(resultNum)