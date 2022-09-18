# 지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 
# 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 
# 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 
# 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 
# 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.

# A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.

# 설계 각각의 친구목록을 생성?

import sys
input = sys.stdin.readline
from collections import deque
# N = int(input())


# friend_data = [list(input()) for _ in range(N)]
# check = [[0 for _ in range(N)] for _ in range(N)]


# # 한다리 건너뛰어서 친구인 사람이있어야 친구가 된다.
# for i in range(N): 
#     for j in range(N):
#         for k in range(N):
#             if j == k : continue # a와 a는 친구가 될 수없다.

#             if (friend_data[j][k] == 'Y' or friend_data[j][i] == 'Y' and friend_data[i][k] == 'Y'): # 
#                 check[j][k] = 1

# answer = 0
# for i in check:
#     answer = max(answer, sum(i))

# print(answer)
# print(friend_data)
# print(check)
