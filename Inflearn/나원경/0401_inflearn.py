#92 키보드 고장
import sys
# csv 파일 불러오기
# data = 0
# def sol(d):
#     pass
# sol(data)


#93 페이지 교체 - 선입선출 알고리즘
# pages = ['BCBAEBCE','ABCABCABC','ABCDABEABCDE','ABCEDF','ABCDABEA']
# frames = [3,3,4,0,3]
# for i in range(5):
#     frame = frames[i]
#     memory = []
#     idx=0
#     sigan = 0
#     if frame > 0:
#         for page in pages[i]:
#             if page not in memory:
#                 if len(memory) == frame:
#                     memory.pop(idx % frame)
#                 memory.insert(idx % frame, page)
#                 idx += 1
#                 sigan += 6
#                 # print(page,memory)
#             else:
#                 sigan += 1
#     else:
#         sigan = len(pages[i])*10
#     print(f'{i+1}: {sigan}')

#94 - 내일 한 번 더

#95 도장찍기
# def rot(matrix,number):
#     result = [[] for _ in range(4)]
#     for i in range(4):
#         for j in range(4):
#             result[i].append(stamp[3-j][i])
#     answer = [list(map(lambda x,y:x+y,matrix[i],result[i])) for i in range(4)]
#     return answer
#
# stamp = [[1,1,1,2],[2,0,0,0],[1,1,1,1],[0,0,0,0]]
# rot_num = 1
# print(rot(stamp,rot_num))