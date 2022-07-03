score = [0,0,0,0,0,0,0,0]

for i in range(8):
    score[i] = int(input())

sorted_score = sorted(score, reverse=True)

print(sum(sorted_score[0:5]))

result_list = []

for s in sorted_score[0:5]:
    result_list.append(score.index(s)+1)

result_list.sort()

print(' '.join(map(str, result_list)))