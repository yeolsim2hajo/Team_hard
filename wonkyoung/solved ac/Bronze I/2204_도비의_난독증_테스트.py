#230108
# import sys
# new_input = sys.stdin.readline
# while True:
#     n = int(new_input())
#     if n == 0:
#         break
#     first = 'z'*20
#     lower_first = first
#     for _ in range(n):
#         word = new_input().rstrip()
#         lower_word = word.lower()
#         if lower_word < lower_first:
#             lower_first = lower_word
#             first = word
#     print(first)


# 함수형
def find_first(n):
    first = lower_first = 'z'*20
    for _ in range(n):
        word = new_input().rstrip()
        lower_word = word.lower()
        if lower_word < lower_first:
            lower_first = lower_word
            first = word
    return first
import sys
new_input = sys.stdin.readline
while True:
    n = int(new_input())
    if n == 0:
        break
    print(find_first(n))


#
def find_first(n):
    first = lower_first = 'z'*20
    for _ in range(n):
        word = new_input().rstrip()
        lower_word = word.lower()
        if lower_word < lower_first:
            lower_first = lower_word
            first = word
    return first
import sys
new_input = sys.stdin.readline
n = int(new_input())
while n:
    print(find_first(n))
    n = int(new_input())
