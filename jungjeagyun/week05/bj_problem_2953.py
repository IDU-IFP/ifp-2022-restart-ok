ppl_list = [[],[],[],[],[]]
score_list = []
score_dict = {}

for i in range(1,6):
    ppl_list[i-1] = list(input().split())
    score = sum(map(int,ppl_list[i-1]))
    score_list.append(score)
    score_dict[i] = sum(map(int, ppl_list[i-1]))

max_score = max(score_list)

for key, value in score_dict.items():
    if value == max_score:
        print(key, sum(map(int, ppl_list[key-1])))
