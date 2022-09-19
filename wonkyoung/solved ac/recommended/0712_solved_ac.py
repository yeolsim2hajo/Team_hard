#1972 놀라운 문자열 - new_input 안 쓰면 시간 더 늘어남
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     def is_surprising():
#         for i in range(1,n-1):
#             arr = set()
#             for j in range(n-i):
#                 new = data[j] + data[j+i]
#                 if new in arr:
#                     return 0
#                 arr.add(new)
#         return 1
#
#     while True:
#         data = new_input().rstrip()
#         n = len(data)
#         if data == '*':
#             return
#         if is_surprising():
#             print(f'{data} is surprising.')
#         else:
#             print(f'{data} is NOT surprising.')
# main()

# print 위치 바꿈 - 약간 더 걸림
# def main():
#     def is_surprising():
#         for i in range(1,n-1):
#             arr = set()
#             for j in range(n-i):
#                 new = data[j] + data[j+i]
#                 if new in arr:
#                     print(f'{data} is NOT surprising.')
#                     return
#                 arr.add(new)
#         print(f'{data} is surprising.')
#
#     while True:
#         data = input()
#         n = len(data)
#         if data == '*':
#             return
#         is_surprising()
# main()


# 시간 약간 더 걸림
# def main():
#     def is_surprising():
#         for i in range(1,n-1):
#             arr = set()
#             for j in range(n-i):
#                 new = data[j] + data[j+i]
#                 if new in arr:
#                     return 0
#                 arr.add(new)
#         return 1
#     answer = ['is NOT surprising.', 'is surprising.']
#     while True:
#         data = input()
#         n = len(data)
#         if data == '*':
#             return
#         print(data,answer[is_surprising()])
#
# main()
