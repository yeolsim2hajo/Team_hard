# 백준 20922 겹치는 건 싫어

import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
lst = list(map(int,input().rstrip().split()))

ans = 0
_dict = {}
left, right = 0, 0
while right < n:
    r_cnt = _dict.get(lst[right],0)
    if r_cnt < k:
        _dict[lst[right]] = _dict.get(lst[right],0) + 1
        right+=1
    else:
        _dict[lst[left]] = _dict.get(lst[left],0) - 1
        left+=1
    answer = max(ans, right-left)

print(ans)