# 백준 17124 두 개의 배열
# 시간초과 나서 이분탐색으로 다시 풀어봄!

import sys
input = sys.stdin.readline

def abc(k, s, e):
    a, gap = 21e8, 21e8
    while s <= e:
        mid = (s+e)//2
        if lstm[mid] == k:
            return k
        elif lstm[mid] > k:
            e = mid-1
        else:
            s = mid+1
        if abs(lstm[mid]-k) < gap:
            gap = abs(lstm[mid]-k)
            a = lstm[mid]
        elif abs(lstm[mid]-k) == gap:
            if lstm[mid] < a:
                a = lstm[mid]
    return a

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    lstn = list(map(int, input().split()))
    lstm = list(map(int, input().split()))
    lstm.sort()
    ans = 0
    for i in range(n):
        rst = lstn[i]
        ans += abc(rst, 0, m-1)
    print(ans)