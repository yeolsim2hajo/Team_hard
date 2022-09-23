# 백준 1942 디지털시계

import sys
import datetime
from datetime import timedelta
input = sys.stdin.readline

for i in range(3):
    s, e = input().split()
    S = int(s.replace(":", ""))
    E = int(e.replace(":", ""))
    s1, s2, s3 = map(int, s.split(":"))
    e1, e2, e3 = map(int, e.split(":"))
    t = datetime.datetime(2021, 1, 1, s1, s2, s3)
    T = t.strftime('%H%M%S')
    rst, ans = 1, 0
    if int(T)%3 == 0:
        ans += 1
    check = datetime.datetime(2021, 1, 1, e1, e2, e3)
    check = check.strftime('%H%M%S')
    while True:
        if T == check:
            break
        t = t + timedelta(seconds=rst)
        T = t.strftime('%H%M%S')
        if int(T)%3==0:
            ans+=1
    print(ans)