
import sys
input = sys.stdin.readline

N = int(input())
numbers1 = list(map(int, input().split()))
M = int(input())
numbers2 = list(map(int, input().split()))

numbers1_idx = 0
numbers2_idx = 0
for i in range(M):
    for k in range(N):
        if numbers2[i] == numbers1[k]:
            print(1)
    else:
        print(0)
           
            
