#230122
# 틀림
def solution(nums):
    max_num = sum(nums[-3:])
    numbers = set(range(7, max_num+1, 2))
    for i in range(3, max_num, 2):
        now = 3*i
        while now <= max_num:
            numbers.discard(now)
            now += 2*i
    cnt = 0
    length = len(nums)
    # print(numbers, max_num)
    def plus_numbers(level, total, start):
        nonlocal cnt
        if level == 3:
            if total in numbers:
                cnt += 1
            return
        for i in range(start, length):
            plus_numbers(level+1, total+nums[i], i+1)
    plus_numbers(0,0,0)
    return cnt