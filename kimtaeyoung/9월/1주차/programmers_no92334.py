# 신고 결과 받기

''' 문제 설명
이용자의 ID가 담긴 문자열 배열 id_list,
각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report,
정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때,
각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.
'''

# 풀이


def solution(id_list, report, k):
    report = set(report)
    users = {id: [] for id in id_list}
    reported_users = {id: 0 for id in id_list}
    answer = [0] * len(id_list)

    for r in report:
        id, report_id = r.split()
        users[id] += [report_id]
        reported_users[report_id] += 1

    for index, report_users in enumerate(users.values()):
        for r in report_users:
            if reported_users[r] >= k:
                answer[index] += 1

    return answer
