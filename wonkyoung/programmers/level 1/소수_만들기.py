#230122
# 틀림
# def solution(nums):
#     max_num = sum(nums[-3:])
#     numbers = set(range(7, max_num+1, 2))
#     for i in range(3, max_num, 2):
#         now = 3*i
#         while now <= max_num:
#             numbers.discard(now)
#             now += 2*i
#     cnt = 0
#     length = len(nums)
#     # print(numbers, max_num)
#     def plus_numbers(level, total, start):
#         nonlocal cnt
#         if level == 3:
#             if total in numbers:
#                 cnt += 1
#             return
#         for i in range(start, length):
#             plus_numbers(level+1, total+nums[i], i+1)
#     plus_numbers(0,0,0)
#     return cnt

#230201
def solution(nums):
    nums.sort()
    max_num = sum(nums[-3:])
    # print(max_num)
    prime_num = set(range(7, max_num+1, 2))
    for i in range(3, max_num+1, 2):
        now = 3*i
        while now <= max_num:
            prime_num.discard(now)
            now += 2*i

    cnt = 0
    length = len(nums)
    # print(prime_num, max_num)
    def plus_numbers(level, total, start):
        nonlocal cnt
        if level == 3:
            if total in prime_num:
                cnt += 1
            return
        for i in range(start, length):
            plus_numbers(level+1, total+nums[i], i+1)
    plus_numbers(0,0,0)
    return cnt
'''
테스트 1 〉	통과 (0.69ms, 10.2MB)
테스트 2 〉	통과 (0.92ms, 10.3MB)
테스트 3 〉	통과 (0.23ms, 10.3MB)
테스트 4 〉	통과 (0.18ms, 10.3MB)
테스트 5 〉	통과 (1.04ms, 10.2MB)
테스트 6 〉	통과 (1.40ms, 10.4MB)
테스트 7 〉	통과 (0.22ms, 10.3MB)
테스트 8 〉	통과 (3.16ms, 10.4MB)
테스트 9 〉	통과 (0.67ms, 10.2MB)
테스트 10 〉	통과 (2.94ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 10.4MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.11ms, 10.2MB)
테스트 14 〉	통과 (0.04ms, 10.2MB)
테스트 15 〉	통과 (0.06ms, 10.2MB)
테스트 16 〉	통과 (4.99ms, 10.3MB)
테스트 17 〉	통과 (4.17ms, 10.2MB)
테스트 18 〉	통과 (0.60ms, 10.2MB)
테스트 19 〉	통과 (0.60ms, 10.3MB)
테스트 20 〉	통과 (4.60ms, 10.2MB)
테스트 21 〉	통과 (4.25ms, 10.3MB)
테스트 22 〉	통과 (1.26ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (3.66ms, 10.4MB)
테스트 25 〉	통과 (3.62ms, 10.4MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
'''


def solution(nums):
    nums.sort()
    max_num = sum(nums[-3:])
    prime_num = set(range(7, max_num+1, 2))
    cnt = 0
    def find_prime_num():
        for i in range(3, max_num+1, 2):
            now = 3*i
            while now <= max_num:
                prime_num.discard(now)
                now += 2*i

    def plus_numbers():
        nonlocal cnt
        length = len(nums)
        for i in range(length-2):
            one = nums[i]
            for j in range(i+1, length-1):
                two = one + nums[j]
                for k in range(j+1, length):
                    if two + nums[k] in prime_num:
                        cnt += 1
    find_prime_num()
    plus_numbers()
    return cnt
'''
테스트 1 〉	통과 (0.29ms, 10.3MB)
테스트 2 〉	통과 (0.37ms, 10.4MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.08ms, 10.2MB)
테스트 5 〉	통과 (0.40ms, 10.4MB)
테스트 6 〉	통과 (0.74ms, 10.2MB)
테스트 7 〉	통과 (0.18ms, 10.2MB)
테스트 8 〉	통과 (1.38ms, 10.2MB)
테스트 9 〉	통과 (0.27ms, 10.3MB)
테스트 10 〉	통과 (1.33ms, 10.2MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
테스트 16 〉	통과 (2.51ms, 10.4MB)
테스트 17 〉	통과 (1.94ms, 10.4MB)
테스트 18 〉	통과 (0.61ms, 10.2MB)
테스트 19 〉	통과 (0.62ms, 10.2MB)
테스트 20 〉	통과 (2.25ms, 10.2MB)
테스트 21 〉	통과 (2.12ms, 10.2MB)
테스트 22 〉	통과 (0.85ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (1.88ms, 10.4MB)
테스트 25 〉	통과 (1.91ms, 10.3MB)
테스트 26 〉	통과 (0.01ms, 10.3MB)
'''