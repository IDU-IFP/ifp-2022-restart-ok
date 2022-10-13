dayNum = int(input())
lastNumOfCarNumber = (list(map(int, input().split(' '))))
offense_cars = 0

for i in lastNumOfCarNumber:
    if i == dayNum:
        offense_cars = offense_cars + 1

print(offense_cars)