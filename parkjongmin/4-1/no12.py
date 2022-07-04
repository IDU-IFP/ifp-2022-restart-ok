#5565_영수증
price,b1,b2,b3,b4,b5,b6,b7,b8,b9 = map(int, input().split())
b10 = price - (b1+b2+b3+b4+b5+b6+b7+b8+b9)
print(b10)