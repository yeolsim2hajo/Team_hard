#221108
# N = int(input())
# cards = sorted(map(int, input().split()))
# M = int(input())
# numbers = list(map(int, input().split()))
# start, end = 0, N-1
# for number in numbers:
#     while start <= end:
#         mid = (start + end) // 2
#         if cards[mid] < number:
#             start = mid + 1
#         elif cards[mid] > number:
#             end = mid - 1
#         else:
#             print(1, end=' ')
#             break
#     else:
#         print(0, end=' ')
#     start, end = 0, N-1

# 인덱스 + 정렬
# N = int(input())
# cards = sorted(map(int, input().split()))
# M = int(input())
# numbers = input().split()
# for i in range(M):
#     numbers[i] = (i, int(numbers[i]))
# numbers.sort(key= lambda x: x[1])
# start, end = 0, N-1
# result = [0] * M
# for i, number in numbers:
#     while start <= end:
#         mid = (start + end) // 2
#         if cards[mid] < number:
#             start = mid + 1
#         elif cards[mid] > number:
#             end = mid - 1
#         else:
#             result[i] = 1
#             break
#     start, end = mid, N-1
# print(*result)


# 함수로
# def card_game():
#     N = int(input())
#     cards = sorted(map(int, input().split()))
#     M = int(input())
#     numbers = list(map(int, input().split()))
#
#     def find_number(number):
#         start, end = 0, N - 1
#         while start <= end:
#             mid = (start + end) // 2
#             if cards[mid] < number:
#                 start = mid + 1
#             elif cards[mid] > number:
#                 end = mid - 1
#             else:
#                 return 1
#         return 0
#
#     for number in numbers:
#         print(find_number(number), end=' ')
# card_game()


# for문으로 받기 - 시간, 메모리 더나옴
# def card_game():
#     cnt = []
#     cards = []
#     for _ in range(2):
#         cnt.append(int(input()))
#         cards.append(list(map(int, input().split())))
#     cards[0].sort()
#
#     def find_number(number):
#         start, end = 0, cnt[0] - 1
#         while start <= end:
#             mid = (start + end) // 2
#             if cards[0][mid] < number:
#                 start = mid + 1
#             elif cards[0][mid] > number:
#                 end = mid - 1
#             else:
#                 return 1
#         return 0
#
#     for number in cards[1]:
#         print(find_number(number), end=' ')
# card_game()


# set 사용
# def card_game():
#     N = int(input())
#     cards = set(input().split())
#     M = int(input())
#     numbers = input().split()
#
#     for number in numbers:
#         print(int(number in cards), end=' ')
# card_game()


# set + list 사용
# def card_game():
#     N = int(input())
#     cards = set(input().split())
#     M = int(input())
#     numbers = input().split()
#
#     for i in range(M):
#         numbers[i] = int(numbers[i] in cards)
#     return numbers
# print(*card_game())


# if else - 시간 덜 걸림
# def card_game():
#     N = int(input())
#     cards = set(input().split())
#     M = int(input())
#     numbers = input().split()
#
#     for i in range(M):
#         numbers[i] = 1 if numbers[i] in cards else 0
#     return numbers
# print(*card_game())


# 안 쓰는 input 변수 할당 X
# def card_game():
#     input()
#     cards = set(input().split())
#     M = int(input())
#     numbers = input().split()
#
#     for i in range(M):
#         numbers[i] = 1 if numbers[i] in cards else 0
#     return numbers
# print(*card_game())


# int 없앰
def card_game():
    N = input()
    cards = set(input().split())
    M = int(input())
    numbers = input().split()

    for i in range(M):
        numbers[i] = 1 if numbers[i] in cards else 0
    return numbers
print(*card_game())