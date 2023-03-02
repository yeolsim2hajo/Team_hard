#230302
# def josephus_perm(N, K):
#     removed = []
#     people = list(map(str, range(1, N+1)))
#     index = K - 1
#     length = N
#     for _ in range(N-1):
#         removed.append(people.pop(index))
#         length -= 1
#         index = (index - 1 + K) % length
#     removed.append(people[0])
#     return ', '.join(removed)
#
# N, K = map(int, input().split())
# print(f'<{josephus_perm(N, K)}>')

#
# def josephus_perm(N, K):
#     removed = ''
#     people = list(map(str, range(1, N+1)))
#     index = K - 1
#     length = N
#     for _ in range(N-1):
#         removed += people.pop(index) + ', '
#         length -= 1
#         index = (index - 1 + K) % length
#     removed += people[0]
#     return removed
#
# N, K = map(int, input().split())
# print(f'<{josephus_perm(N, K)}>')


#
def josephus_perm():
    N, K = map(int, input().split())
    removed = ''
    people = list(map(str, range(1, N+1)))
    index = K - 1
    length = N
    for _ in range(N-1):
        removed += people.pop(index) + ', '
        length -= 1
        index = (index - 1 + K) % length
    removed += people[0]
    return removed

print(f'<{josephus_perm()}>')