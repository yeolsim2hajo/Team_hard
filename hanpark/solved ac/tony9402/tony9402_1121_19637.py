import sys
input = sys.stdin.readline

def check(lst, num):
    s, e = 0, len(lst)-1
    ans = 0
    while s <= e:
        m = (s+e)//2
        if int(lst[m][1]) >= num:
            e = m-1
            ans = m
        else:
            s = m+1
    return ans

N, M = map(int, input().strip().split())
lst = [input().strip().split() for _ in range(N)]
for _ in range(M):
    num = int(input())
    print(lst[check(lst, num)][0])