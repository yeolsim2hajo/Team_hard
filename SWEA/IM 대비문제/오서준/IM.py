# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import sys
sys.stdin=open('case.text')


                                   #방 들어가기
# def go(arr):
#     bucket = [0] * 201
#     for i in range(len(arr)):
#         if (arr[i][0] + 1) // 2== (arr[i][1] + 1) // 2:
#             bucket[(arr[i][0] + 1) // 2] += 1
#         elif arr[i][0] < arr[i][1]:
#             for j in range((arr[i][0] + 1) // 2, ((arr[i][1] + 1) // 2)+1):
#                 bucket[j] += 1
#         else:
#             for j in range((arr[i][1] + 1) // 2, ((arr[i][0] + 1) // 2)+1):
#                 bucket[j] += 1
#     max = 0
#     for i in range(len(bucket)):
#         if max < bucket[i]:
#             max = bucket[i]
#     return max
#
#
# TC = int(input())
# for t in range(1, TC + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{t} {go(arr)}')






                                        #어디에 단어가 들어갈 수 있을까(오답)
#
# def move(arr, M, K):
#     arrr = [[0]*(M+2) for _ in range(M+2)]
#     cnt = 0
#     ar=[0]
#     for i in range(K):
#         ar=ar+[1]
#     ar=ar+[0]
#
#     for i in range(M):
#         for j in range(M):
#             arrr[i+1][j+1]=arr[i][j]
#
#     for i in range(len(arrr)):
#         arr_row = []
#         arr_col = []
#         for k in range(K+2):
#             arr_row = arr_row + [arrr[i][k]]
#             arr_col = arr_col + [arrr[k][i]]
#
#         for j in range(M - K + 1):
#             if arr_row == ar:
#                 cnt += 1
#             if arr_col == ar:
#                 cnt += 1
#             if j>=M-K:
#                 break
#             arr_row = arr_row[1:] + [arrr[i][j +K+2]]
#             arr_col = arr_col[1:] + [arrr[j +K+2][i]]
#
#     return cnt
#
#
#
# TC = int(input())
# for t in range(1, TC + 1):
#      M, K = map(int, input().split())
#      arr = [list(map(int, input().split())) for _ in range(M)]
#      print(f'#{t} {move(arr, M, K)}')
#








                                        #사다리
# def Ladder(arr):
#     arr=arr[-1: :-1]
#     for j in range(100):
#         if arr[0][j]==2:
#             break
#     for i in range(1,100):
#         if j!=0 and arr[i][j-1]==1:
#             while j!=0 and arr[i][j-1]==1:
#                 j-=1
#         elif j!=99 and arr[i][j+1]==1:
#             while j!=99 and arr[i][j+1]==1:
#                 j+=1
#     return j
#
# TC=10
# for _ in range(10):
#     t=int(input())
#     arr=[list(map(int,input().split())) for _ in range(100)]
#     print(f'#{t} {Ladder(arr)}')


                                            #백만장자

# def coins(ar,N):
#
#     Max=0
#     y= 0
#     s=0
#
#     while s<=N-1:
#         sum1 = 0
#         max1 = 0
#         for i in range(s,N):
#             if max1<ar[i]:
#                 max1=ar[i]
#                 y=i
#         for i in range(s,y):
#             sum1+=ar[i]
#         Max+=max1*(y-s)-sum1
#         s=y+1
#     return Max
# # sum1+=ar[i]
# #         if max1<ar[i]*(i+1)-sum1:
# #             max1=ar[i]*(i+1)-sum1
#
# TC=int(input())
# for t in range(1,TC+1):
#     N=int(input())
#     ar=list(map(int,input().split()))
#     print(f'#{t} {coins(ar,N)}')


