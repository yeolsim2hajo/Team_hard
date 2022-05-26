#2805 나무 자르기
# N, M = map(int,input().split())
# tree = list(map(int,input().split()))
# tree.sort()
# total = sum(tree)
# start = 0
# end = N-1
# value = 0
# while start <= end:
#     mid = (start+end)//2
#     if total - tree[mid] * N >= M:
#         temp = 0
#         for branch in tree:
#             if branch > tree[mid]:
#                 temp += branch - tree[mid]
#         if temp == M:
#             value = tree[mid]
#             break
#         elif temp > M:
#             start = mid
#             continue
#     end = mid
# if tree




# for height in range(max_val-1,0,-1):
#     total = 0
#     for branch in tree:
#         if branch > height:
#             total += branch - height
#     if total >= M:
#         break
# print(height)

#10828 스택
N = int(input())
stack = []
size = 0
top = -1
for _ in range(N):
    command = input().strip()
    if command[-1] == 'e':
        print(size)
    elif command[-1] == 'y':

        stack.append(command[1])
        size += 1
        top = command[1]
    elif command[0] == 'pop':
        if size:
            print(stack.pop())
            size -= 1
            top = stack[-1] if size else -1
        else:
            print(-1)
    elif command[0] == 'size':
        print(size)
    elif command[0] == 'empty':
        print(int(not size))
    else:
        print(top)

