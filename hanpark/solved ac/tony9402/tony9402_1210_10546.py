# 백준 10546 배부른 마라토너

import sys
input = sys.stdin.readline

N = int(input().strip())
dic1, dic2 = dict(), dict()
for _ in range(N):
    a = input().strip()
    if a not in dic1:
        dic1[a] = 1
    else:
        dic1[a] += 1
for _ in range(N-1):
    a = input().strip()
    if a not in dic2:
        dic2[a] = 1
    else:
        dic2[a] += 1
for d in dic1.keys():
    #  참가자에는 있지만 완주자에는 없다면 그게 정답
    if d not in dic2:
        print(d)
        break
    else:
        #  참가자의 value와 완주자의 value가 다르다면 그게 정답
        if dic1[d] != dic2[d]:
            print(d)
            break