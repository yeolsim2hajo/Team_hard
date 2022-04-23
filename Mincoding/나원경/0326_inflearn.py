#80 순열과 조합
# def comb(arg=0,start=0,val=''):
#     global cnt
#     if arg == n:
#         lst.append(val)
#         return
#     for i in range(start,length):
#         comb(arg+1,i+1,val+jaeum[i])
#
# jaeum = input().split(',')
# length = len(jaeum)
# n = int(input())
# lst = []
# comb()
# print(lst,len(lst),sep='\n')


#81 지뢰찾기
# flag = [] # 지뢰 없이 깃발만 있는 리스트
# minesweeper = [] #지뢰를 찾은 리스트
# for i in range(5):
#     flag.append(input('깃발 값과 함께 입력하세요 : ').split(' '))
# minesweeper = [[0]*5 for _ in range(5)]
# for i in range(5):
#     for j in range(5):
#         minesweeper[i][j] = flag[i][j]
#
# for i in range(5):
#     for j in range(5):
#         if minesweeper[i][j] == '1':
#             minesweeper[i][j] = 'f'
#             for di,dj in (0,1), (0,-1), (1,0), (-1,0):
#                 y,x = i+di,j+dj
#                 if 0 <= y < 5 and 0 <= x < 5 and minesweeper[y][x] != '1':
#                     minesweeper[y][x] ='*'
#     # print(*flag[i])
#     print(*minesweeper[i])

'''
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 0
'''
