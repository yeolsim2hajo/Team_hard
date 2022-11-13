import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
s, e = 1, int(lst[-1]-int(0)) # 최소거리와 최대거리
while s <= e:
    m = (s+e)//2
    ans, x = 1, lst[0] # 설치된 공유기 갯수, 이전 공유기 설치된 곳
    for i in range(1, len(lst)):
        if lst[i]-x >= m:
            x = lst[i]
            ans += 1
    if ans >= c:
        s = m+1
    else:
        e = m-1
print(e)
