import sys
new_input = sys.stdin.readline
K, H, Q = map(int, new_input().split())
tree = []
for _ in range(Q):
    start, end = map(int, new_input().split())
