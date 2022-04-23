# 내장 모듈-re
import re

def solution(s):
    answer = []
    l = re.split('[0-9]번: ', s)[1:]
    for i in range(len(l)):
        l[i] = list(map(int, l[i].replace(' ', '').split(',')))
    for i in l:
        for j in i:
            if j in answer:
                pass
            else:
                answer.append(j)
    return answer

i = '1번: 3,1 2번: 4 3번: 2,1,3 4번: 2,1,3,4'
solution(i)