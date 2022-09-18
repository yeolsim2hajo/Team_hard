# 중복 신고는 set으로 제거
# split을 이용해서, reports의 요소에서 신고자/신고한 이름을 추출
# reports를 순회해서, 신고당한 사람 cnt 세기
# 만약 k번 이상 신고당했으면 answer에 각각 누가 메일을 받을 것인지 세주기

# 푸는 방법 자체는 간단했지만, dict를 이용해서, 아래처럼 깔끔하게 구현하는 게 어려웠음
    # 특히, ele.split()[1] 부분
def solution(id_list, reports, k):
    answer = [0] * len(id_list) # 메일 받을 횟수들
    newReports = {x: 0 for x in id_list} # reports를 set형태로 재구성(중복제거)
    
    for ele in set(reports): # 처음 순회해서, 신고당한 사람 횟수 올리기
        newReports[ele.split()[1]] += 1
        
    for ele2 in set(reports): # 그리고, 위의 신고당한 횟수가 k이상이면, 신고한 사람에게 보낼 메일 횟수 +1
        if newReports[ele2.split()[1]] >= k:
            answer[id_list.index(ele2.split()[0])] += 1
            
    return answer
    