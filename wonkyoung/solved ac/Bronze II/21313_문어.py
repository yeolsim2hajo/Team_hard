#221213
# N = int(input())
# numbers = ['1','2'] * (N//2)
# if N%2:
#     numbers += ['3']
# print(' '.join(numbers))


# 함수
def find_numbers(N):
    numbers = ['1', '2'] * (N // 2)
    if N % 2:
        numbers += ['3']
    return ' '.join(numbers)

N = int(input())
print(find_numbers(N))
