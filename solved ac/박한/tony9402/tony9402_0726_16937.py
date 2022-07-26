# 백준 16937 두 스티커

import sys
input = sys.stdin.readline
h, w = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if (arr[i][0]+arr[j][0]<=h and max(arr[i][1], arr[j][1])<=w) or (arr[i][1]+arr[j][1]<=w and max(arr[i][0], arr[j][0])<=h):
            ans = max(ans, arr[i][0]*arr[i][1]+arr[j][0]*arr[j][1])
        if (arr[i][1]+arr[j][0]<=h and max(arr[i][0], arr[j][1])<=w) or (arr[i][0]+arr[j][1]<=w and max(arr[i][1], arr[j][0])<=h):
            ans = max(ans, arr[i][0]*arr[i][1]+arr[j][0]*arr[j][1])
        if (arr[i][1]+arr[j][1]<=h and max(arr[i][0], arr[j][0])<=w) or (arr[i][0]+arr[j][0]<=w and max(arr[i][1], arr[j][1])<=h):
            ans = max(ans, arr[i][0]*arr[i][1]+arr[j][0]*arr[j][1])
        if (arr[i][0]+arr[j][1]<=h and max(arr[i][1], arr[j][0])<=w) or (arr[i][1]+arr[j][0]<=w and max(arr[i][0], arr[j][1])<=h):
            ans = max(ans, arr[i][0]*arr[i][1]+arr[j][0]*arr[j][1])
print(ans)