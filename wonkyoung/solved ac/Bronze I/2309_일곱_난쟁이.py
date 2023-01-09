#230109
# dfs
# heights = [int(input()) for _ in range(9)]
# path = []
# finished = False
# def dfs(level=0, total=0, start=0):
#     global finished
#     if finished:
#         return
#     if level == 7:
#         if total == 100:
#             path.sort()
#             print(*path, sep='\n')
#             finished = True
#         return
#     for i in range(start, 9):
#         height = heights[i]
#         path.append(height)
#         dfs(level+1, total+height, i+1)
#         path.pop()
# dfs()

# dfs
# heights = [int(input()) for _ in range(9)]
# path = []
# finished = False
# def dfs(level=0, total=sum(heights), start=0):
#     global finished, heights
#     if finished:
#         return
#     if level == 2:
#         if total == 100:
#             sorted_height = heights[:]
#             for element in path:
#                 sorted_height.remove(element)
#             sorted_height.sort()
#             print(*sorted_height, sep='\n')
#             finished = True
#         return
#     for i in range(start, 9):
#         height = heights[i]
#         path.append(height)
#         dfs(level+1, total-height, i+1)
#         path.pop()
# dfs()

# for
# def find_dwarf():
#     heights = [int(input()) for _ in range(9)]
#     total = sum(heights)
#     for i in range(9):
#         total_temp = total - heights[i]
#         for j in range(i+1, 9):
#             if total_temp - heights[j] == 100:
#                 heights.pop(j)
#                 heights.pop(i)
#                 heights.sort()
#                 print(*heights, sep='\n')
#                 return
# find_dwarf()


