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


#
#230305
# def solution(phone_book):
#     phone_numbers = [set() for _ in range(21)]
#     phone_book.sort(key=lambda num: (len(num), num))
#     for ref in phone_book:
#         index = len(ref)
#         prefix = ref[0]
#         for i in range(1, index):
#             if prefix in phone_numbers[i]:
#                 return False
#             prefix += ref[i]
#         phone_numbers[index].add(ref)
#     return True
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.4MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.2MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (2.07ms, 10.3MB)
테스트 15 〉	통과 (2.53ms, 10.5MB)
테스트 16 〉	통과 (9.89ms, 10.5MB)
테스트 17 〉	통과 (7.42ms, 10.4MB)
테스트 18 〉	통과 (8.68ms, 10.7MB)
테스트 19 〉	통과 (5.08ms, 10.7MB)
테스트 20 〉	통과 (13.26ms, 10.7MB)
효율성  테스트
테스트 1 〉	통과 (7.64ms, 11.3MB)
테스트 2 〉	통과 (7.74ms, 11.4MB)
테스트 3 〉	통과 (859.19ms, 53.9MB)
테스트 4 〉	통과 (489.38ms, 40.8MB)
'''

def solution(phone_book):
    phone_numbers = [set() for _ in range(21)]
    phone_book.sort(key=lambda num: len(num))
    for ref in phone_book:
        index = len(ref)
        prefix = ref[0]
        for i in range(1, index):
            if prefix in phone_numbers[i]:
                return False
            prefix += ref[i]
        phone_numbers[index].add(ref)
    return True
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.4MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.1MB)
테스트 14 〉	통과 (1.67ms, 10.2MB)
테스트 15 〉	통과 (1.91ms, 10.3MB)
테스트 16 〉	통과 (4.55ms, 10.2MB)
테스트 17 〉	통과 (9.93ms, 10.5MB)
테스트 18 〉	통과 (6.89ms, 10.3MB)
테스트 19 〉	통과 (4.36ms, 10.4MB)
테스트 20 〉	통과 (5.34ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (1.63ms, 10.7MB)
테스트 2 〉	통과 (1.59ms, 10.9MB)
테스트 3 〉	통과 (590.28ms, 41.4MB)
테스트 4 〉	통과 (224.99ms, 29.4MB)
'''