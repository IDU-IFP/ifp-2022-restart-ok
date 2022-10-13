count = 0

for i in (input().split(',')):
    try:
        int(i)
        count = count+1
    except:
        pass

print(count)