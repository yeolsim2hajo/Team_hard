#221019
import sys
from heapq import heappop, heappush
new_input = sys.stdin.readline
N = int(new_input())
info = []
for i in range(1, N+1):
    score, submit_cnt, upload_time = map(int, new_input().split())
    heappush(info, (-score, submit_cnt, upload_time, i))
print(heappop(info)[-1])