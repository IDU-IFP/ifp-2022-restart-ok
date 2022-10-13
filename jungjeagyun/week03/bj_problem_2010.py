import sys
pbar = int(sys.stdin.readline())
sum = 0
for i in range(pbar):
    sum += int(sys.stdin.readline())
print(sum - (pbar - 1))