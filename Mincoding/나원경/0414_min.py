# #lv 34
# # 재귀로 만드는 Binary Search
# def y_or_n(lst):
#     global exist
#     half = len(lst)//2
#     if lst == []:
#         return
#     if number == lst[half]:
#         exist = 'O'
#         return
#     if visited[half] == False:
#         path.append(lst[half])
#         visited[half] = True
#         if number < lst[half]:
#             y_or_n(lst[:half])
#         else:
#             y_or_n(lst[half:])
# arr = [4,4,5,7,8,10,20,22,23,24]
# visited = [False]*10
# number = int(input())
# path = []
# exist = 'X'
# y_or_n(arr)
# print(exist)


#2 자동차 기름 채우기
# oil = input()
# left = 0
# right = 9
# while left < right:
#     mid = (left+right)//2
#     if oil[mid] == '#':
#         left = mid+1
#     else:
#         right = mid-1
# print(f'{(mid+1)*10}%')