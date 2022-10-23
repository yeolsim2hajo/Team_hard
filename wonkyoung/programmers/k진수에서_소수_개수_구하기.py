# def solution(n, k):
#     answer = 0
#     number = ''
#     while n > 0:
#         number = str(n%k) + number
#         n //= k
#     length = len(number)
#     start = end = -1
#     prime_number = set()
#     max_number = 1

#     def is_prime(num):
#         nonlocal max_number
#         if not num:
#             return False
#         num = int(num)
#         if num == 2:
#             return True
#         elif num%2 == 0 or num == 1:
#             return False
#         elif num <= max_number:
#             return num in prime_number
#         else:
#             new_set = {i for i in range(max_number+1, num+1)}
#             for i in range(max_number+1, num):
#                 temp_set = set(new_set)
#                 if i in new_set:
#                     for j in temp_set:
#                         if j%i == 0:
#                             new_set.remove(j)
#             max_number = num
#             prime_number.update(new_set)
#             return num in prime_number

#     for i in range(length):
#         if number[i] == '0':
#             start, end = end+1, i
#             answer += is_prime(number[start:end])
#     answer += is_prime(number[end+1:])

#     return answer


# def solution(n, k):
#     answer = 0
#     number = ''
#     while n > 0:
#         number = str(n%k) + number
#         n //= k
#     length = len(number)
#     start = end = -1

#     def is_prime(num):
#         if not num:
#             return False
#         num = int(num)
#         if num == 2:
#             return True
#         elif num%2 == 0 or num == 1:
#             return False

#         for i in range(3, num, 2):
#             if num%i == 0:
#                 return False
#         return True

#     for i in range(length):
#         if number[i] == '0':
#             start, end = end+1, i
#             answer += is_prime(number[start:end])
#     answer += is_prime(number[end+1:])

#     return answer


# def solution(n, k):
#     answer = 0
#     number = ''
#     while n > 0:
#         number = str(n % k) + number
#         n //= k
#     length = len(number)
#     start = end = -1
#     prime_number = set()
#     max_number = 1
#
#     def is_prime(num):
#         nonlocal max_number
#         if not num:
#             return False
#         num = int(num)
#         if num == 2:
#             return True
#         elif num % 2 == 0 or num == 1:
#             return False
#         elif max_number >= num:
#             return num in prime_number
#
#         new_set = {i for i in range(max_number + 1, num + 1, 2)}
#         n = len(new_set)
#         for _ in range(n):
#             rand = new_set.pop()
#             for i in range(3, num, 2):
#                 if rand % i == 0:
#                     break
#             prime_number.add(rand)
#         return num in prime_number
#
#     for i in range(length):
#         if number[i] == '0':
#             start, end = end + 1, i
#             answer += is_prime(number[start:end])
#     answer += is_prime(number[end + 1:])
#
#     return answer


#220927
# def solution(n, k):
#     from math import isqrt
#     def convert(num, div):
#         number = ''
#         while num > 0:
#             number = str(num % div) + number
#             num //= div
#         return number
#
#     def is_prime(num):
#         nonlocal answer
#         if num > '1':
#             num = int(num)
#             limit = isqrt(num)
#             for i in range(2, limit + 1):
#                 if num % i == 0:
#                     return
#             answer += 1
#
#     answer = 0
#     converted_num = convert(n, k)
#     target = ''
#     for num in converted_num:
#         if num != '0':
#             target += str(num)
#         else:
#             is_prime(target)
#             target = ''
#     is_prime(target)
#     return answer

# split 사용
def solution(n, k):
    from math import isqrt
    def convert(num, div):
        number = ''
        while num > 0:
            number = str(num % div) + number
            num //= div
        return number

    def is_prime(num):
        nonlocal answer
        if num > '1':
            num = int(num)
            limit = isqrt(num)
            for i in range(2, limit + 1):
                if num % i == 0:
                    return
            answer += 1

    answer = 0
    converted_num = convert(n, k).split('0')
    for num in converted_num:
        if num != '':
            is_prime(num)
    return answer
