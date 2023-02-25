#230225
# N = int(input())
# for _ in range(N):
#     A, B = input().split()
#     if len(A) != len(B):
#         print(f'{A} & {B} are NOT anagrams.')
#     else:
#         check = {}
#         for alp in A:
#             if check.get(alp):
#                 check[alp] += 1
#             else:
#                 check[alp] = 1
#         for alp in B:
#             if check.get(alp):
#                 check[alp] -= 1
#             else:
#                 print(f'{A} & {B} are NOT anagrams.')
#                 break
#         else:
#             print(f'{A} & {B} are anagrams.')

#
def is_anagram():
    A, B = input().split()
    if len(A) != len(B):
        return f'{A} & {B} are NOT anagrams.'
    check = {}
    for alp in A:
        if check.get(alp):
            check[alp] += 1
        else:
            check[alp] = 1
    for alp in B:
        if check.get(alp):
            check[alp] -= 1
        else:
            return f'{A} & {B} are NOT anagrams.'
    return f'{A} & {B} are anagrams.'

N = int(input())
for _ in range(N):
    print(is_anagram())