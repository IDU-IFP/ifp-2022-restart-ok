#10984_내 학점을 구해줘
T = int(input())
for _ in range(T):
    N = int(input())
    TC = 0
    TG = 0
    for _ in range(N):
        C, G = map(str, input().split())
        TC += int(C)
        TG += float(C) * float(G)
    print(TC, round(TG / TC, 1)) # 라운드 함수