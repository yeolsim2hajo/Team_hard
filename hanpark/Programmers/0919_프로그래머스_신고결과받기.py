# 프로그래머스 신고 결과 받기

import collections
def solution(id_list, report, k):
    answer = []
    l1, l2 = collections.defaultdict(list), collections.defaultdict(int)  # l1는 list형 딕셔너리, l2는 int형 딕셔너리로
    for n in range(len(report)):
        a, b = report[n].split()
        if b not in l1[a]:
            l1[a].append(b)
            l2[b] += 1
    for i in id_list:
        rst = 0
        for j in l1[i]:
            if l2[j] >= k:
                rst += 1
        answer.append(rst)  
    return answer