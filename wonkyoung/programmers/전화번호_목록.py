# 220916
# 전화번호 목록 - 해시
# 시간 초과
# def solution(phone_book):
#     N = len(phone_book)
#     phone_book.sort(key = lambda x:len(x))
#     for i in range(N):
#         prefix = phone_book[i]
#         length = len(prefix)
#         for j in range(i+1, N):
#             phone_no = phone_book[j]
#             if prefix == phone_no[:length]:
#                 return False
#     return True


# 시간 초과
# def solution(phone_book):
#     phone_book.sort(key = lambda x:len(x))
#     first = {str(i):[] for i in range(10)}
#     for phone_no in phone_book:
#         num = phone_no[0]
#         for element in first[num]:
#             M = len(element)
#             if element == phone_no[:M]:
#                 return False
#         first[num].append(phone_no)
#     return True

# 시간 초과
# def solution(phone_book):
#     first = {str(i):[] for i in range(10)}
#     for phone_no in phone_book:
#         num = phone_no[0]
#         for element in first[num]:
#             M = min(len(element), len(phone_no))
#             if element[:M] == phone_no[:M]:
#                 return False
#         first[num].append(phone_no)
#     return True



# def solution(phone_book):
#     numbers = {}
#     for phone_no in phone_book:
#         val = numbers.get(phone_no)
#         if val:
#             length = min(len(phone_no),len(val))
#             for i in range(length):
#                 if phone_no[i] != val[i]:
#                     break
#             else:
#                 return False
#         else:
#             numbers[phone_no[0]] = phone_no
#     return True