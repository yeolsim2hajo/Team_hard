# 백준 13413 오셀로 재배치

import sys
input = sys.stdin.readline

T = int(input())
lst = []
for i in range(T):
    N = int(input())
    word1 = list(input())
    word2 = list(input())
    result = []
    Bsum = 0
    Wsum = 0
    cnt = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            result.append(word1[i])

    for i in result:
        if i == 'B':
            Bsum +=1
        else:
            Wsum +=1

    if Bsum != 0 and Wsum != 0:
        cnt = max(Bsum,Wsum)
    else:
        cnt += Bsum + Wsum

    lst.append(cnt)

for i in lst:
    print(i)