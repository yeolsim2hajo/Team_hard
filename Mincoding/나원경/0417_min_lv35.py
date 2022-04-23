#1 Heap 정렬 구현하기

# heap = list(map(str,input()))
# heap = [''] + heap
# def find_max():
#     length = len(heap)
#     for i in range(length-2):
#         idx = length - 1 - i
#         while idx > 1:
#             top = idx//2
#             if heap[idx] < heap[top]:
#                 break
#             heap[idx],heap[top] = heap[top], heap[idx]
#             idx = top
# for _ in range(1,len(heap)):
#     find_max()
#     print(heap.pop(1),end='')
#     heap.insert(1,heap[-1])
#     heap.pop(-1)


