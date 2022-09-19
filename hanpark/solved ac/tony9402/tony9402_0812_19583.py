# 백준 19583 싸이버개강총회

import sys
input = sys.stdin.readline
S, E, Q = input().split()
s, e, q = int("".join(S.split(":"))), int("".join(E.split(":"))), int("".join(Q.split(":")))
dic, ans = dict(), 0
while 1:
    try:
        T, name = input().split()
        time = int("".join(T.split(":")))
        if time <= s:
            dic[name] = 1
        elif e <= time <= q:
            if dic.get(name):
                if dic[name] == 1:
                    dic[name] = 2
                    ans += 1
    except:
        break
print(ans)