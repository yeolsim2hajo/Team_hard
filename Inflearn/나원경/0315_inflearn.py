#38 호준이의 아르바이트
# scores = list(map(int, input().split()))
# cnt = 0
# for _ in range(3):
#     max_i = []
#     for i in range(len(scores)):
#         if max(scores) == scores[i]:
#             cnt += 1
#             max_i.append(i)
#     for j in range(len(max_i)-1,-1,-1):
#         scores.pop(max_i[j])
# print(cnt)


#39 오타 수정하기
# word = input()
# print(word.replace('q','e'))

# for문 이용
# for alp in word:
#     if alp == 'q':
#         print('e',end='')
#     else:
#         print(alp,end='')


#40 놀이동산에 가자
# limit = int(input())
# N = int(input())
# total = cnt = 0
# for i in range(N):
#     total += int(input())
#     if total <= limit:
#         cnt += 1
#     else:
#         print(cnt)
#         break


# Chapter 1-5

#41 소수판별
# N = int(input())
# if N in [2,3]:
#     print('YES')
# elif N % 2 == 0:
#     print('NO')
# else:
#     for number in range(3,N,2):
#         if N % number == 0:
#             print('NO')
#             break
#     else:
#         print('YES')


#42 2020년
# def solution():
#     a, b = map(int, input().split())
#     ans = 2
#     month = [31,29,31,30,31,30,31,31,30,31,30,31]
#     ans += sum(month[:a-1])+b
#     return ans % 7
#
# name = ['SUN','MON','TUE','WED','THU','FRI','SAT']
# print(name[solution()])


#43 10진수를 2진수로
# N = int(input())
# binary = []
# while N > 1:
#     binary.append(N%2)
#     N //= 2
# if N != 0:
#     print(1, *binary[::-1], sep='')
# else:
#     print(0)

# 재귀 이용
# N = int(input())
# def binary(arg=N):
#     if arg == 0:
#         return
#     binary(arg//2)
#     print(arg%2,end='')
# binary()


#44 각 자리수의 합
# N = list(map(int,input()))
# print(sum(N))


#45 time함수 사용하기
# import time # 1970년 1월 1일 기준 초단위
# print(int(time.time()//(60*60*24*365)+1970))
# print(time.time_ns())
# print(time.daylight)
# print(time.process_time())
# print(time.tzset())


#46 str
# int_to_str = ''
# for i in range(1,21):
#     int_to_str += str(i)
# lst = list(map(int, int_to_str))
# print(sum(lst))


#47 set
# people = [('이호준','01050442903'),
#           ('이호상','01051442904'),
#           ('이준호','01050342904'),
#           ('이호준','01050442903'),
#           ('이준','01050412904'),
#           ('이호','01050443904'),
#           ('이호준','01050442903')]
# print(len(set(people)))

#48 대소문자 바꿔서 출력하기
# word = input()
# print(word.swapcase())


#49 최댓값 구하기
# numbers = map(int, input().split())
# print(max(numbers))


# 50 버블정렬 구현
# def bubble(n,data):
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#     for i in range(n):
#         print(data[i], end=' ')
#
# n = int(input())
# data = list(map(int, input().split()))
#
# bubble(n,data)

#51 merge sort
# def merge_sort(lst):
#     len_lst = len(lst)
#     if len_lst <= 1:
#         return lst
#     mid = len_lst//2
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[:mid])
#     ans = []
#
#     while left and right:
#         if left:
#             ans.append(left.pop(0))
#         else:
#             ans.append(right.pop(0))
#
#     while left:
#         ans.append(left.pop(0))
#     while right:
#         ans.append(right.pop(0))
#     return ans
#
# test_lst = [100,145,165,45,170,175,173,171]
# # 빈칸 - 뭔지 모르겠음
#
# print(merge_sort(test_lst))
#
#
# #52 퀵
# def quick_sort(lst):
#     len_lst = len(lst)
#     if len_lst <= 1:
#         return lst
#     pivot = lst.pop(len_lst//2)
#     left = []
#     right = []
#
#     for i in range(len_lst-1):
#         if lst[i] < pivot:
#             left.append(lst[i])
#         else:
#             right.append(lst[i])
#     return left+[pivot]+right
#
# test_lst = input().split(' ')
# # 빈칸 - 뭔지 모르겠음
#
# print(quick_sort(test_lst))


#53 괄호 문자열
# munja = input()
# cnt = 0
# for element in munja:
#     if element == '(':
#         cnt += 1
#     elif element == ')':
#         cnt -= 1
# if cnt:
#     print('NO')
# else:
#     print('YES')


#54 연속되는 수
numbers = list(map(int, input().split()))
max_num = max(numbers)
min_num = min(numbers)
if len(numbers) != len(list(range(min_num,max_num+1))):
    print('NO')
else:
    print('YES')

# if max_num - min_num != len(numbers)-1: print('NO')


#55 하노이의 탑
path = []
def hanoi(number,start,end,mid):
    if number == 1:
        path.append([start,end])
        return
    # 경유 기둥으로 n-1개 옮기기
    hanoi(number-1,start,mid,end)
    # 가장 큰 원판 목표기둥으로
    path.append([start,end])
    # 경유 기둥과 시작 기둥 바꾸기
    hanoi(number-1,mid,end,start)

user_input = int(input())
hanoi(user_input,'A','C','B')

print(len(path))


#56 list
nationwidth = {
    'Korea':220877,
    'Rusia': 17098242,
    'China' : 9596961,
    'France' : 543965,
    'Japan' : 377915,
    'England' : 242900}
ans = 'Rusia'
for key in nationwidth.keys():
    if nationwidth[ans