# lv 23
#1 1등, 2등, 3등 선물주기
# def present(arg=0):
#     if arg == 3:
#         print(*path, sep='')
#         return
#     for i in range(4):
#         if used[i] == 0:
#             path[arg] = people[i]
#             used[i] = 1
#             present(arg+1)
#             used[i] = 0
#
# people = input()
# path = ['']*3
# used = [0]*4
# present()


#2 다툰친구 B와 T
# alp = input()
# path = ['']*4
# cnt = 0
#
# def datum(arg=0):
#     global cnt
#     if arg == 4:
#         cnt += 1
#         return
#     for i in range(4):
#         if alp[i] == 'B' and path[arg-1] == 'T':
#             continue
#         elif alp[i] == 'T' and path[arg-1] == 'B':
#             continue
#         path[arg] = alp[i]
#         datum(arg+1)
#         path[arg] = ''
# datum()
# print(cnt)


#3 ABC초콜릿
# N = int(input())
# cnt = 0
# choco = ['A','B','C']
# path = ['']*N
# def select(arg=0):
#     global cnt
#     if arg == N:
#         cnt += 1
#         return
#     for i in range(3):
#         if arg >= 2 and choco[i] == path[arg-1] == path[arg-2]:
#             continue
#         path[arg] = choco[i]
#         select(arg+1)
#         path[arg] = ''
#
# select()
# print(cnt)

# 산타소년단
# N = int(input())
# member = ['B','T','S','K','R']
# used = [0]*5
# path = ['']*N
# cnt = 0
# def group(arg=0):
#     global cnt
#     if arg == N:
#         cnt += 1
#         return
#     for i in range(5):
#         if used[i] or (arg == N-1 and used[2] == 0 and i != 2):
#             continue
#         used[i] = 1
#         path[arg] = member[i]
#         group(arg+1)
#         used[i] = 0
#
# group()
# print(cnt)


# 미안하다 친구야
# friends = ['E','W','A','B','C']
# exclude = input()
# friends = [x for x in friends if x != exclude]
# used = [0]*4
# path = ['']*4
# def boat(arg=0):
#     if arg == 4:
#         print(*path,sep='')
#         return
#     for i in range(4):
#         if used[i] == 0:
#             path[arg] = friends[i]
#             used[i] = 1
#             boat(arg+1)
#             used[i] = 0
# boat()


#6 다섯종류의 숫자카드
# cards = list(map(int,input()))
# path = [0]*4
# cnt = 0
# def choose(arg=0):
#     global cnt
#     if arg == 4:
#         cnt += 1
#         return
#     for i in range(5):
#         if arg >= 1 and not (-3 <= cards[i] - path[arg-1] <= 3):
#             continue
#         path[arg] = cards[i]
#         choose(arg+1)
#
# choose()
# print(cnt)


# lv 23.5

# 왼쪽, 오른쪽 이동
# def move(arg):
#     global arr
#     if arg == 'R':
#         for i in range(len(arr)):
#             if i != len(arr) - 1:
#                 arr[i], arr[-1] = arr[-1], arr[i]
#     else:
#         for i in range(len(arr)):
#             if i != len(arr) - 1:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
# arr = [3,5,1,9,7]
# for _ in range(4):
#     direction = input()
#     move(direction)
# print(*arr)

# 배열 변화 없음
# for _ in range(4):
    # if direction == 'R':
    #     for i in range(-1,len(arr)-1):
    #         print(arr[i],end=' ')
    # else:
    #     for i in range(len(arr)-1):
    #         print(arr[i+1],end=' ')
    #     print(arr[0])


# 암살자 존휙
# position = [input().split() for _ in range(3)]
# flag = 0
# for i in range(2):
#     for j in range(i+1,3):
#         if position[i][0] == position[j][0] or position[i][1] == position[j][1]:
#             flag = 1
#             break
#     if flag:
#         print('위험')
#         break
# else:
#     print('안전')


# 네모네모 더하기
# arr = [[0]*4 for _ in range(4)]
# for i in range(3):
#     arr[i][:3] = list(map(int, input().split()))
#     arr[i][3] = sum(arr[i])
# for i in range(3):
#     arr[3][i] = sum([arr[j][i] for j in range(3)])
# for i in range(3):
#     arr[3][3] += arr[i][i]
# for i in range(4):
#     print(*arr[i])

# 다른 방법 이용해보기


# 숫자 transformation
# arr = [list(map(str,data)) for data in ['3541','1123','6712']]
# numbers = input().split()
# for i in range(3):
#     for j in range(4):
#         for k in range(4):
#             if k < 3 and arr[i][j] == numbers[k]:
#                 arr[i][j] = numbers[k+1]
#                 break
#             elif arr[i][j] == numbers[3]:
#                 arr[i][j] = numbers[0]
#     print(*arr[i])


# 자기자리 찾기
# arr = list(map(int, input().split()))
# pivot = arr[0]
# a = 1
# b = len(arr)-1
# while a <= b:
#     if a <= b and arr[b] < pivot < arr[a]:
#         arr[a], arr[b] = arr[b], arr[a]
#     if arr[a] <= pivot:
#         a += 1
#     if arr[b] >= pivot:
#         b -= 1
#
# arr[0], arr[b] = arr[b], arr[0]
# print(*arr)


# 황금좌표 찾기
# hard = [list(map(str,data)) for data in ['ABCD','BBAB','CBAC','BAAA']]
# user = [list(map(str,input())) for _ in range(4)]
# gold = [0]*4
#
# for i in range(4):
#     for j in range(4):
#         if hard[i][j] == user[i][j]:
#             gold[ord(hard[i][j]) - ord('A')] += 1
# number = gold.index(max(gold))
# print(chr(number + ord('A')))

# 다른 방법