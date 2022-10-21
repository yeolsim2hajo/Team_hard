#221021
# word = input()
# N = len(word)
# result = 'z' * N
# piece = [''] * 3
# for i in range(1, N-1):
#     piece[0] = word[:i]
#     for j in range(i+1, N):
#         piece[1] = word[i:j]
#         piece[2] = word[j:]
#         new_word = ''
#         for k in range(3):
#             new_word += piece[k][::-1]
#         result = min(result, new_word)
# print(result)


# heap - 시간 더 걸리는 대신, 메모리 줄어듦
# from heapq import heappush, heappop
# word = input()
# N = len(word)
# result = []
# piece = [''] * 3
# for i in range(1, N-1):
#     piece[0] = word[:i]
#     for j in range(i+1, N):
#         piece[1] = word[i:j]
#         piece[2] = word[j:]
#         new_word = ''
#         for k in range(3):
#             new_word += piece[k][::-1]
#         heappush(result, new_word)
# print(heappop(result))


# 한꺼번에 처리 - 시간 더 걸림
word = input()
N = len(word)
piece = [0] * 4
result = 'z' * N
for i in range(1, N-1):
    piece[1] = i
    for j in range(i+1, N):
        piece[2] = j
        piece[3] = N
        new_word = ''
        for k in range(1,4):
            new_word += word[piece[k-1]:piece[k]][::-1]
        result = min(result, new_word)
print(result)



