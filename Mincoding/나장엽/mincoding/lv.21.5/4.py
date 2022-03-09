# arr = [list(input()) for _ in range(4)]

# for i in range(4):
#     for j in range(3):
#         if arr[i][j] == 'A' :
#             y_a = i
#             x_a = j
#         if arr[i][j] == 'C' :
#             y_c = i
#             x_c = j
#         if arr[i][j] == 'T' :
#             y_t = i
#             x_t = j
#         if arr[i][j] == 'K' :
#             y_k = i
#             x_k = j


# arr[y_t][x_t], arr[3][0] = arr[3][0], arr[y_t][x_t]
# arr[y_k][x_k], arr[3][1] = arr[3][1], arr[y_k][x_k]
# arr[y_c][x_c], arr[3][2] = arr[3][2], arr[y_c][x_c]
# arr[y_a][x_a], arr[2][0] = arr[2][0], arr[y_a][x_a]


# for i in range(4):
#     for k in range(3):
#         print(arr[i][k], end='')
#     print()


# def move(arr):
#     for i in range(3):
#         for j in range(3,-1,-1):
#             if arr[j][i]!='_':
#                 while j<3 and arr[j+1][i]=='_':
#                     arr[j][i],arr[j+1][i]= arr[j+1][i],arr[j][i]
#                     j+=1
#     return arr
# # 도저히 못품. 코드 참고함
# # 거꾸로 탐색하면서 _가 아닐때,  while문 진행  arr[j][i] 밑에 언더바가 있으면, swap한다
# # T = 2,0 _ = 3,0 에 있을 때, swap을 진행, _ = 2,0 T = 3,0 으로 변경되고, 다시 반복문 진행
# # j = 3이 되고 , while문 종료, for문 진행
# # j = 1이 되고, [1][0] -> _ 무시
# # j = 0이 되고 , [0][0] -> while문으로 들어감
# # 조건 충족, 0,0 1,0 swap
# # j += 1 / j =1
# # while문 조건 충족
# # 1,0 과 2,0 SWAP
# # 문자 밑에 언더바가 2개 있으면 while문을 통해 처리...! while문에 종료조건 j < 3 필수.
# arr=[list(input()) for _ in range(4)]
# x = move(arr)

# for i in range(4):
#     for j in range(3):
#         print(x[i][j], end='')
#     print()


def down(n):
    flag = 0
    for i in range(3, -1, -1):
        if arr[i][n] == '_':
            for k in range(2, -1, -1):
                if arr[k][n] != '_':
                    arr[i][n] = arr[k][n]
                    arr[k][n] = '_'
                    flag = 1
                    break
            if flag == 0:
                break


arr = [list(input()) for _ in range(4)]
for i in range(3):
    down(i)


for i in range(4):
    for j in range(3):
        print(arr[i][j], end='')
    print()
