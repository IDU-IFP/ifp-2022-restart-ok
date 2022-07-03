fp = [0,0,0,0,0,0,0,0,0,0] # 내린 사람
tp = [0,0,0,0,0,0,0,0,0,0] # 탄 사람
current_ppl = 0 # 열차에 있던 순간
current_ppl_list = [0,0,0,0,0,0,0,0,0,0] # 열차에 있던 순간

for i in range(10):
    fp[i], tp[i] = map(int,input().split()) # 저장
    current_ppl = current_ppl - fp[i] + tp[i] # 현재 인간들을 저장
    current_ppl_list[i] = current_ppl # 현재 순간의 인간 수를 리스트에 저장

print(max(current_ppl_list))