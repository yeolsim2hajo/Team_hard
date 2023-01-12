#220615
# import sys,heapq
# N = int(input())
# new_input = sys.stdin.readline
# table = []
# for i in range(N):
#     row = list(map(int,new_input().split()))
#     table.extend(row)
#     heapq.heapify(table)
#     if len(table) > N:
#         for _ in range(N):
#             heapq.heappop(table)
# print(table[0])