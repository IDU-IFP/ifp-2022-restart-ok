h, m = map(int, input().split())
rt = int(input())

hour = (h+((m+rt)//60)) % 24 # % 24 생각 못 했음.
minute = (m + rt) % 60       # % 60 생각 못 했음.

print(hour, minute)