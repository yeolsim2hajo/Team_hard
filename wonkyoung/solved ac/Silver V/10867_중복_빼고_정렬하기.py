#221218
# N = int(input())
# numbers = list(map(int, input().split()))
# bucket = [0] * 2001
# for number in numbers:
#     index = number + 1000
#     if bucket[index] == 0:
#         bucket[index] = 1
# answer = []
# for i in range(2001):
#     if bucket[i] == 1:
#         answer.append(str(i-1000))
# print(' '.join(answer))


# 함수로
# def main():
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     bucket = [0] * 2001
#     for number in numbers:
#         index = number + 1000
#         if bucket[index] == 0:
#             bucket[index] = 1
#     answer = []
#
#     for i in range(2001):
#         if bucket[i] == 1:
#             answer.append(str(i-1000))
#     return ' '.join(answer)
# print(main())

# set 사용 - 메모리 덜 나옴, 시간 더 걸림
# def main():
#     N = int(input())
#     numbers = set(map(int, input().split()))
#     bucket = [0] * 2001
#     for number in numbers:
#         index = number + 1000
#         bucket[index] = 1
#     answer = []
#
#     for i in range(2001):
#         if bucket[i] == 1:
#             answer.append(str(i - 1000))
#     return ' '.join(answer)
#
# print(main())


# set + sorted
# def main():
#     N = int(input())
#     numbers = set(map(int, input().split()))
#     answer = map(str,sorted(numbers))
#     return ' '.join(answer)
#
# print(main())
