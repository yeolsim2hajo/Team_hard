import sys
input = sys.stdin.readline

N, M = map(int, input().split())
add = {}

for _ in range(N):
    site, ps = input().split()
    add[site] = ps

for _ in range(M):
    print(add[input().rstrip()])