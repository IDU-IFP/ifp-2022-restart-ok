import math

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

print(math.gcd(num1, num2))
print(math.lcm(num1, num2))