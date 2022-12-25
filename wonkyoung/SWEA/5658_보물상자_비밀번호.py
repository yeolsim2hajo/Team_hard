#221225
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     numbers = input()
#     quarter = N//4
#     all_numbers, final_numbers = set(), set()
#     conv_alp = {chr(55+i):i for i in range(10, 16)}
#     keys = set(conv_alp.keys())
#
#     def conv_number(number):
#         answer = 0
#         length = len(number)
#         number = number[::-1]
#         for i in range(length):
#             num = number[i]
#             if num in keys:
#                 answer += conv_alp[num] * (16 ** i)
#             else:
#                 answer += int(num) * (16 ** i)
#         return int(answer)
#
#     for _ in range(N):
#         for i in range(4):
#             number = numbers[quarter*i:quarter*(i+1)]
#             all_numbers.add(number)
#         numbers = numbers[-1] + numbers[:N-1]
#     for number in all_numbers:
#         final_numbers.add(conv_number(number))
#     print(f'#{tc} {sorted(final_numbers, reverse=True)[K-1]}')


# 여러 번 시도
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    initial_numbers = input()
    quarter = N//4
    all_numbers, final_numbers = set(), list()
    conv_alp = {}
    for i in range(16):
        if i < 10:
            conv_alp[str(i)] = i
        else:
            conv_alp[chr(55 + i)] = i
    keys = set(conv_alp.keys())

    def conv_number(number):
        answer, length = 0, len(number)
        rev_number = number[::-1]
        for i in range(length):
            num = rev_number[i]
            answer += conv_alp[num] * (16 ** i)
        return answer

    numbers = initial_numbers
    for _ in range(N):
        for i in range(4):
            number = numbers[quarter*i:quarter*(i+1)]
            all_numbers.add(number)
        numbers = numbers[-1] + numbers[:N-1]
        if numbers == initial_numbers:
            break
    for number in all_numbers:
        final_numbers.append(conv_number(number))
    final_numbers = sorted(final_numbers, reverse=True)
    print(f'#{tc} {final_numbers[K-1]}')


# 함수형
conv_alp = {}
for i in range(16):
    if i < 10:
        conv_alp[str(i)] = i
    else:
        conv_alp[chr(55 + i)] = i
keys = set(conv_alp.keys())
def find_pw():
    N, K = map(int, input().split())
    initial_numbers = input()
    quarter = N // 4
    all_numbers, final_numbers = set(), list()

    def conv_number(number):
        answer, length = 0, len(number)
        rev_number = number[::-1]
        for i in range(length):
            num = rev_number[i]
            answer += conv_alp[num] * (16 ** i)
        return answer

    numbers = initial_numbers
    for _ in range(N):
        for i in range(4):
            number = numbers[quarter * i:quarter * (i + 1)]
            all_numbers.add(number)
        numbers = numbers[-1] + numbers[:N - 1]
        if numbers == initial_numbers:
            break
    for number in all_numbers:
        final_numbers.append(conv_number(number))
    final_numbers = sorted(final_numbers, reverse=True)
    return final_numbers[K-1]

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc} {find_pw()}')