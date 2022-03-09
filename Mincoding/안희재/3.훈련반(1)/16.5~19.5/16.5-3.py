T = list(map(int,input().split()))

original_arr = [[T[0],T[1],T[2]], [T[3],T[4],T[5]]]
# original_arr = [[1,3,5], [2,6,-5]]

max_num = max(T)
min_num = min(T)

min_x = 0 # position 
min_y = 0
max_x = 0
max_y = 0

for i in range(2):
    for j in range(3):
        if max_num == original_arr[i][j]:
            max_x, max_y = i, j
        if min_num == original_arr[i][j]:
            min_x, min_y = i, j

print(f'({max_x},{max_y})')
print(f'({min_x},{min_y})')



# T = list(map(int,input().split()))

# original_arr = [[T[0],T[1],T[2]], [T[3],T[4],T[5]]]
# # original_arr = [[1,3,5], [2,6,-5]]

# max_num = max(T)
# min_num = min(T)
# max_position = (0,0)
# min_position = (0,0)

# for i in range(2):
#     for j in range(3):
#         if max_num == original_arr[i][j]:
#             max_position = (i,j)
#         if min_num == original_arr[i][j]:
#             min_position = (i,j)

# print(max_position)
# print(min_position)
# 어어.. 이렇게 했더니 오답.. 설마 (1, 1) 이렇게 띄워져서 출력된다고..? 설마?!
# ㅆㅂ.. 맞네.. 위 처럼 했더니 정답!!