#230210
# N, H, W = map(int, input().split())
# before = ['?'] * N
# for _ in range(H):
#     after = input()
#     for i in range(N):
#         index = W*i
#         if before[i] == '?':
#             for j in range(W):
#                 if after[index] != '?':
#                     before[i] = after[index]
#                     break
#                 index += 1
# print(''.join(before))

#
# N, H, W = map(int, input().split())
# before = ['?'] * N
# for _ in range(H):
#     after = input()
#     index = 0
#     for i in range(N):
#         for j in range(W):
#             if before[i] == '?' and after[index] != '?':
#                 before[i] = after[index]
#             index += 1
# print(''.join(before))


#
# def find_before():
#     N, H, W = map(int, input().split())
#     before = ['?'] * N
#     for _ in range(H):
#         after = input()
#         index = 0
#         for i in range(N):
#             for j in range(W):
#                 if before[i] == '?' and after[index] != '?':
#                     before[i] = after[index]
#                 index += 1
#     return ''.join(before)
# print(find_before())


#
# def find_before():
#     N, H, W = map(int, input().split())
#     before = ['?'] * N
#     for _ in range(H):
#         after = input()
#         index = 0
#         for i in range(N):
#             for _ in range(W):
#                 if before[i] == '?' and after[index] != '?':
#                     before[i] = after[index]
#                 index += 1
#     return ''.join(before)
# print(find_before())


#
# N, H, W = map(int, input().split())
# before = ['?'] * N
# for _ in range(H):
#     after = input()
#     index = 0
#     for i in range(N):
#         if before[i] == '?':
#             for j in range(W):
#                 if after[index+j] != '?':
#                     before[i] = after[index+j]
#                     break
#         index += W
# print(''.join(before))



#
def find_before():
    N, H, W = map(int, input().split())
    before = ['?'] * N
    for _ in range(H):
        after = input()
        index = 0
        for i in range(N):
            if before[i] == '?':
                for j in range(W):
                    if after[index + j] != '?':
                        before[i] = after[index + j]
                        break
            index += W
    return ''.join(before)

print(find_before())