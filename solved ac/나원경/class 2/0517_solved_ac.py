#10814 나이순 정렬
# 시간 초과
# N = int(input())
# members = []
# for i in range(N):
#     member = input().split()
#     member[0] = int(member[0])
#     idx = -1
#     for j in range(i-1,-1,-1):
#         if members[j][0] > member[0]:
#             idx = j
#         else:
#             members.insert(idx,member)
#             break
#     else:
#         members.insert(idx, member)
# for i in range(N):
#     print(*members[i])


# N = int(input())
# members = []
# for _ in range(N):
#     members.append(input().split())
#     members[-1][0] = int(members[-1][0])
# members.sort(key=lambda x:x[0])
# for i in range(N):
#     print(*members[i])