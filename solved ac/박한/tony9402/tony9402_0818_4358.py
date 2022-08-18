# 백준 4358 생태학

import sys
input = sys.stdin.readline
dic, rst = dict(), 0
while 1:
    name = input()
    if name == "":
        break
    if dic.get(name):
        dic[name] += 1
    else:
        dic[name] = 1
    rst += 1
dic1 = sorted(dic.items())
d = len(dic)
for i in range(d):
    per = round((dic1[i][1]/rst)*100, 4)
    print(dic1[i][0], '%.4f' %per)

# 출력형식이 잘못되었습니다 - 왜?