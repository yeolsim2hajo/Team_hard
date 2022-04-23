#82 수학 괄호 파싱
# def math(e):
#     open = 0
#     for element in e:
#         if element == '(':
#             open += 1
#         elif element == ')':
#             if open:
#                 open -= 1
#             else:
#                 return False
#     if open:
#         return False
#     else:
#         return True
#
# while 1:
#     order = input('데이터 입력(1), 프로그램 종료(2) :')
#     if order == '1':
#         ex = input('데이터를 입력하세요 : ')
#         print(math(ex))
#     else:
#         break

#83 수학 괄호 파싱2 - 다시
# def math(e):
#     small = 0
#     medium = 0
#     for element in e:
#         if element == '(':
#             small += 1
#         elif element == '{':
#             medium += 1
#         elif element == ')':
#             if small:
#                 small -= 1
#             else:
#                 return False
#         elif element == '}':
#             if medium:
#                 medium -= 1
#             else:
#                 return False
#     if small or medium:
#         return False
#     else:
#         return True
#
# while 1:
#     order = input('데이터 입력(1), 프로그램 종료(2) : ')
#     if order == '1':
#         ex = input('데이터를 입력하세요 : ')
#         print(math(ex))
#     else:
#         break


#84 숫자 뽑기
# def choose(arg=0,start=0,num=''):
#     global max_num
#     if arg == k:
#         if max_num < int(num):
#             max_num = int(num)
#         return
#     for i in range(start,length):
#         choose(arg+1,i+1,num+n[i])
#
# n = input()
# length = len(n)
# k = int(input())
# max_num = 0
# choose()
# print(max_num)