# 각 유저별로 처리결과 메일을 받은 횟수를 배열에 담아 return
# k번 이상 신고당한 경우, 해당 유저를 신고한 유저에게 이메일 발송
# k번 이상 신고당한 유저는 정지 사실을 메일 
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list, report, k): # 이용자 id, 신고내역, 정지기준 횟수
    check = [0] * len(id_list)
    reporter = {x : 0  for x in id_list}

    # print(reporter) # {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}

    # 신고당한 횟수
    for repo in set(report): 
        reporter[repo.split()[1]] += 1
    # print(reporter) #{'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}

    # 신고 당한 횟수가 k이상이면?
    for repo in set(report):
        if reporter[repo.split()[1]] >= k:
            # 신고한 사람에게 결과 이메일 전송 받는 횟수 count
            check[id_list.index(repo.split()[0])] += 1
    # print(check) # [2, 1, 1, 0]
    return check

print(solution(id_list, report, 2))
