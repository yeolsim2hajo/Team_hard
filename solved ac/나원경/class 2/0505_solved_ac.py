#1181 단어 정렬
N = int(input())
# words = []
# length = [0]*51
# for _ in range(N):
#     words.append(input())
#     length[len(words[-1])] += 1
# len_idx = 1
# while len_idx < 51:
#     if length[len_idx]:
#         word = 'z' * 50
#         for i in range(len(words)):
#             if len(words[i]) == len_idx and word > words[i]:
#                 word = words[i]
#         print(word)
#         words.remove(word)
#         length[len_idx] -= 1
#     else:
#         len_idx += 1
words = set(input() for _ in range(N))
words = list(words)
words.sort(key=lambda x:(len(x),x))
for i in range(len(words)):
    print(words[i])


