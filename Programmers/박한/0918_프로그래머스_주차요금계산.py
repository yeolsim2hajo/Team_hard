# 프로그래머스 주차 요금 계산

import math
def solution(fees, records):
    answer = []
    dic1, dic2 = dict(), dict()
    for n in records:
        a, b, c = n.split()
        a1, a2 = a.split(':')
        t = int(a1)*60 + int(a2)
        if c == "IN":
            dic1[b] = t
        else:
            dic2[b] = dic2.get(b, 0) + (t - dic1[b])
            del dic1[b]
    for d in dic1:
        dic2[d] = dic2.get(d, 0) + (23*60+59) - dic1[d]
    for i, j in sorted(dic2.items()):
        if j > fees[0]:
            answer.append(fees[1] + math.ceil((j-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
    return answer