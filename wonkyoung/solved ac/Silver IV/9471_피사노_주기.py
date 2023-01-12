#221218
def number_condition(number1, number2):
    cnt = 0
    while number1 > 1:
        cnt += 1
        number1, remain = divmod(number1, number2)
        if remain:
            return 0
    return cnt

def find_fibonacci(end):
    pass

def find_remain(number1, number2):
    return number1%number2

def find_length(target):
    if target%2 == 0:
        two = number_condition(target, 2)
        if two:
            return 3 * 2 ** (two-1)

        half_five = number_condition(target // 2, 5)
        if half_five:
            return 6 * half_five

        ten = number_condition(target, 10)
        if ten > 2:
            return 15 * 10 ** (ten - 1)
    else:
        five = number_condition(target, 5)
        if five:
            return 4 * 5 ** five

    limit = min(target ** 2 - 1, total_limit)
    length = len(fibonacci)
    period = list(map(find_remain, fibonacci, [target] * length))
    for i in range(4, length, 2):
        # if target == 987654:
        #     print(i)
        if i >= length:
            for _ in range(2):
                fibonacci.append(fibonacci[-1] + fibonacci[-2])
                period.append(fibonacci[-1] % target)
            length += 2

        if period[i] == period[0]:
            for j in range(i+1, 2*i):
                if j >= length:
                    fibonacci.append(fibonacci[-1] + fibonacci[-2])
                    period.append(fibonacci[-1] % target)
                if period[j] != period[j-i]:
                    break
            else:
                return i
            # if period[:i+1] == period[i+1:2*i]:
            #     return i
    return limit
    for i in range(4, limit, 2):
        # if target == 987654:
        #     print(i)
        if i >= length:
            for _ in range(2):
                fibonacci.append(fibonacci[-1] + fibonacci[-2])
                period.append(fibonacci[-1] % target)
            length += 2

        if period[i] == period[0]:
            for j in range(i+1, 2*i):
                if j >= length:
                    fibonacci.append(fibonacci[-1] + fibonacci[-2])
                    period.append(fibonacci[-1] % target)
                if period[j] != period[j-i]:
                    break
            else:
                return i
            # if period[:i+1] == period[i+1:2*i]:
            #     return i
    return limit

import sys
new_input = sys.stdin.readline
P = int(new_input())
fibonacci = [1, 1, 2]
total_limit = int(5e5)
for _ in range(P):
    N, M = map(int, new_input().split())
    answer = find_length(M)
    print(N, answer)
    total_limit -= answer