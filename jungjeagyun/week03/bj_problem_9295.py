testCase = int(input())

for i in range(testCase):
    num1, num2 = map(int, input().split(' '))
    print(f'Case {i+1}: {num1+num2}')