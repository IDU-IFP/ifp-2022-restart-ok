# 5565 - 영수증
totalPrice = int(input())
count = 0

for i in range(9):
    bookPrice = int(input())
    count += bookPrice

print(totalPrice - count)