# 이분탐색으로 구현
# 2중for문으로는 시간초과

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

x = int(input())
count = 0 # x를 만족하는 쌍의 개수.

start, end = 0, n - 1

while start != end : 
    if arr[start] + arr[end] == x:
        count += 1
        start += 1
    elif arr[start] + arr[end] > x :
        end -= 1
    else :
        start += 1

print(count)

  