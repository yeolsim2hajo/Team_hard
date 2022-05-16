
import sys
input = sys.stdin.readline
N = int(input())
numbers1 = set(map(int, input().split()))
M = int(input())
numbers2 = list(map(int, input().split()))

# 시간초과
# for i in range(M):
#     for k in range(N):
#         if numbers2[i] == numbers1[k]:
#             print(1)
#             break
#     else:
#         print(0)
           
            
for number2 in numbers2:
    print(1) if number2 in numbers1 else print(0)
