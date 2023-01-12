#221105
# 다시 시도
# import sys
# new_input = sys.stdin.readline
# T = int(new_input())
# for _ in range(T):
#     N = int(new_input())
#     # 1위이면 무조건 합격
#     # cnt = 2
#     ranks = [[0] * 2]
#     # candidates = set(range(1, N+1))
#     # one = [[] for _ in range(2)]
#     for i in range(1, N+1):
#         document, interview = map(int, new_input().split())
#         ranks.append([document, interview])
#         # ranks[0][document] = i
#         # ranks[1][interview] = i
#         if document == 1:
#             interview_limit = interview
#             # document_one = i
#             # one[0].append((i, interview))
#         if interview == 1:
#             # interview_one = i
#             document_limit = document
#             # one[0].append((i, document))
#     # print(ranks)
#     newcomer = set(range(1, N+1))
#     for i in range(1, N+1):
#         if ranks[i][0] > document_limit or ranks[i][1] > interview_limit:
#             newcomer.remove(i)
#     print(len(newcomer))


# 다시 시도2
# import sys
# new_input = sys.stdin.readline
# T = int(new_input())
# for _ in range(T):
#     N = int(new_input())
#     ranks = [[0] * 2]
#     interview_limit = document_limit = N
#     for _ in range(1, N+1):
#         document, interview = map(int, new_input().split())
#         ranks.append([document, interview])
#         if document == 1:
#             interview_limit = interview
#         if interview == 1:
#             document_limit = document
#     cnt = 0
#     for i in range(1, N+1):
#         if 1 <= ranks[i][0] <= document_limit and 1 <= ranks[i][1] <= interview_limit:
#             cnt += 1
#     print(cnt)


#221106
# 시간 초과
# heap 이용
import sys, heapq
new_input = sys.stdin.readline
T = int(new_input())
for _ in range(T):
    N = int(new_input())
    ranks, interview_list, document_list = set(), [], []
    for i in range(1, N+1):
        document, interview = map(int, new_input().split())
        ranks.add((document, interview))
        heapq.heappush(document_list, (document, interview))
        heapq.heappush(interview_list, (interview, document))
    pre_document_limit = pre_interview_limit = N
    for _ in range(N):
        document_limit, interview_limit = heapq.heappop(document_list), heapq.heappop(interview_list)
        if pre_document_limit < interview_limit[1] and pre_interview_limit < document_limit[1]:
            break
        # limit = min(document_limit[1], interview_limit[1])
        temp = set()
        for rank in ranks:
            if rank[0] <= interview_limit[1] or rank[1] <= document_limit[1]:
                temp.add(rank)
        ranks = set(temp)
        pre_document_limit, pre_interview_limit = interview_limit[1], document_limit[1]
        print(ranks)
    print(len(ranks))
