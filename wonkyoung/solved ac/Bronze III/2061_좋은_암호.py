# 220919
# def password():
#     K, L = map(int, input().split())
#     for i in range(2, L):
#         if K%i == 0:
#             print('BAD', i)
#             return
#     print('GOOD')
# password()

# def password():
#     K, L = map(int, input().split())
#     for i in range(2, L):
#         if K%i == 0:
#             return 'BAD', i
#     return ['GOOD']
# print(*password())

# def password():
#     K, L = map(int, input().split())
#     for i in range(2, L):
#         if K%i == 0:
#             return ['BAD', i]
#     return ['GOOD']
# print(*password())

# 홀짝 나눔
def password():
    K, L = map(int, input().split())
    if L > 2 and K%2 == 0:
        return ['BAD', 2]
    for i in range(3, L, 2):
        if K%i == 0:
            return ['BAD', i]
    return ['GOOD']
print(*password())