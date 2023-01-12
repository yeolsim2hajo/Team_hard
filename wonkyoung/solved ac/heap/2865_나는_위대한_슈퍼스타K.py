#221018
import sys
from heapq import heappush, heappop

new_input = sys.stdin.readline
N, M, K = map(int, new_input().split())
for _ in range(M):
    audition = []
    candidate = new_input().split()
    for i in range(N):
        heappush(audition, (int(candidate[2*i]), float(candidate[2*i+1])))
