#11279 최대 힙
# import sys,heapq
# N = int(input())
# new_input = sys.stdin.readline
# max_heap = []
# for _ in range(N):
#     x = int(new_input())
#     if x:
#         heapq.heappush(max_heap, -x)
#     elif max_heap:
#         print(-heapq.heappop(max_heap))
#     else:
#         print(0)

# 직접 구현
# import sys
# N = int(input())
# new_input = sys.stdin.readline
# max_heap = [0]
# idx = 0

# def push(val):
#     global idx
#     max_heap.append(val)
#     idx += 1
#     son = idx
#     while son > 1:
#         parent = son // 2
#         if max_heap[son] < max_heap[parent]:
#             break
#         max_heap[parent], max_heap[son] = max_heap[son], max_heap[parent]
#         son = parent
# def pop():
#     global idx
#     max_heap[1], max_heap[idx] = max_heap[idx], max_heap[1]
#     answer = max_heap.pop()
#     idx -= 1
#     parent = 1
#     while True:
#         son = parent * 2
#         if son > idx:
#             break
#         if son < idx and max_heap[son] < max_heap[son+1]:
#             son += 1
#         if max_heap[son] < max_heap[parent]:
#             break
#         max_heap[parent], max_heap[son] = max_heap[son], max_heap[parent]
#         parent = son
#     return answer
# for _ in range(N):
#     x = int(new_input())
#     if x:
#         push(x)
#     elif idx:
#         print(pop())
#     else:
#         print(0)



#