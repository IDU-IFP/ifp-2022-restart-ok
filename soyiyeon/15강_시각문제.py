# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):  # 분, 0부터 59까지 증가
        for k in range(60):  # 초, 0부터 59까지 증가
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):  # 시, 분, 초를 문자열 형태로 만들어 더함.
                count += 1

print(count)
