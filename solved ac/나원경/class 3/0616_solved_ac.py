#11286 절댓값 힙
# import heapq, sys
# N = int(input())
# new_input = sys.stdin.readline
# abs_heap = []
# for _ in range(N):
#     data = new_input().rstrip()
#     if data == '0':
#         answer = heapq.heappop(abs_heap)[1] if abs_heap else 0
#         print(answer)
#     else:
#         data = int(data)
#         heapq.heappush(abs_heap,(abs(data), data))

#11399 ATM
# heapq 이용
# import heapq
# N = int(input())
# def minus(number):
#     return -int(number)
# people = list(map(minus,input().split()))
# total = 0
# heapq.heapify(people)
# for _ in range(N):
#     total -= sum(people)
#     heapq.heappop(people)
# print(total)

# sort
# N = int(input())
# people = list(map(int,input().split()))
# total = 0
# people.sort()
# for _ in range(N):
#     total += sum(people)
#     people.pop()
# print(total)

# pop 대신 슬라이싱 - ㅁㅔ모리 차이 없음, 시간 약간 느림
# N = int(input())
# people = list(map(int,input().split()))
# total = 0
# people.sort()
# for i in range(N):
#     total += sum(people[:N-i])
# print(total)


#11403 경로 찾기
# N = int(input())
# graph = [input().split() for _ in range(N)]
# def bfs(start, end):
#     q = [start]
#     visited = [[False] * N for _ in range(N)]
#     first = True
#     while q:
#         now = q.pop(0)
#         if now == end and first is False:
#             return '1'
#         for col in range(N):
#             if graph[now][col] == '1' and visited[now][col] is False:
#                 visited[now][col] = True
#                 graph[start][col] = '1'
#                 q.append(col)
#         first = False
#     return '0'
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == '0':
#             graph[i][j] = bfs(i,j)
#         print(graph[i][j], end=' ')
#     print()

# 마지막만 바꿈 - 위와 큰 차이 없음
#    print(*graph[i])


#11659 구간 합 구하기 4 - 시간 초과
# import sys
# N, M = map(int, input().split())
# numbers = list(map(int,input().split()))
# new_input = sys.stdin.readline
# total = sum(numbers)
# store = set()
# match = {}
# for _ in range(M):
#     start, end = map(int,new_input().split())
#     if (start,end) in store:
#         print(match[(start,end)])
#         continue
#     elif start == end:
#         answer = numbers[start-1]
#     elif (end - start) > N // 2:
#         answer = total - sum(numbers[:start-1]) - sum(numbers[end:])
#     else:
#         answer = sum(numbers[start - 1:end])
#     print(answer)
#     store.add((start,end))
#     match[(start,end)] = answer

'''
5 5
5 4 3 2 1
1 3
2 4
5 5
2 4
1 3
'''