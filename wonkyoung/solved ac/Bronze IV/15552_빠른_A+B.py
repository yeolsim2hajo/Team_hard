#220621
import sys
T = int(input())
new_input = sys.stdin.readline
for _ in range(T):
    A, B = map(int,new_input().split())
    print(A+B)