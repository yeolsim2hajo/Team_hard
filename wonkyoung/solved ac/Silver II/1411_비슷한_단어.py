#230228
# N = int(input())
# words = [input() for _ in range(N)]
# length = len(words[0])
# cnt = 0
# for i in range(N):
#     word1 = words[i]
#     for j in range(i+1, N):
#         match = {alp: '' for alp in word1}
#         word2 = words[j]
#         used = set()
#         for k in range(length):
#             alp1, alp2 = word1[k], word2[k]
#             if match[alp1] == '':
#                 if alp2 in used:
#                     break
#                 else:
#                     match[alp1] = alp2
#                     used.add(alp2)
#             elif match[alp1] != alp2:
#                 break
#         else:
#             cnt += 1
# print(cnt)


#
# def find_similar(N, words):
#     length = len(words[0])
#     cnt = 0
#     for i in range(N):
#         word1 = words[i]
#         for j in range(i+1, N):
#             match = {alp: '' for alp in word1}
#             word2 = words[j]
#             used = set()
#             for k in range(length):
#                 alp1, alp2 = word1[k], word2[k]
#                 if match[alp1] == '':
#                     if alp2 in used:
#                         break
#                     else:
#                         match[alp1] = alp2
#                         used.add(alp2)
#                 elif match[alp1] != alp2:
#                     break
#             else:
#                 cnt += 1
#     return cnt
#
# N = int(input())
# words = [input() for _ in range(N)]
# print(find_similar(N, words))


#
# def find_similar(N, words):
#     length = len(words[0])
#     cnt = 0
#     for i in range(N):
#         word1 = words[i]
#         match = {alp: '' for alp in word1}
#         for j in range(i+1, N):
#             word2 = words[j]
#             used = set()
#             for k in range(length):
#                 alp1, alp2 = word1[k], word2[k]
#                 if match[alp1] == '':
#                     if alp2 in used:
#                         break
#                     else:
#                         match[alp1] = alp2
#                         used.add(alp2)
#                 elif match[alp1] != alp2:
#                     break
#             else:
#                 cnt += 1
#             for key in match:
#                 match[key] = ''
#     return cnt
#
# N = int(input())
# words = [input() for _ in range(N)]
# print(find_similar(N, words))


#
# def find_similar(N, words):
#     length = len(words[0])
#     cnt = 0
#     for i in range(N):
#         word1 = words[i]
#         match = {alp: '' for alp in word1}
#         used = set()
#         for j in range(i+1, N):
#             word2 = words[j]
#             for k in range(length):
#                 alp1, alp2 = word1[k], word2[k]
#                 if match[alp1] == '':
#                     if alp2 in used:
#                         break
#                     else:
#                         match[alp1] = alp2
#                         used.add(alp2)
#                 elif match[alp1] != alp2:
#                     break
#             else:
#                 cnt += 1
#             for key in match:
#                 match[key] = ''
#             used.clear()
#     return cnt
#
# N = int(input())
# words = [input() for _ in range(N)]
# print(find_similar(N, words))


#
def find_similar(N, words):
    length = len(words[0])
    cnt = 0
    def conf_alp():
        for k in range(length):
            alp1, alp2 = word1[k], word2[k]
            if match[alp1] == '':
                if alp2 in used:
                    return 0
                else:
                    match[alp1] = alp2
                    used.add(alp2)
            elif match[alp1] != alp2:
                return 0
        return 1
    for i in range(N):
        word1 = words[i]
        match = {alp: '' for alp in word1}
        used = set()
        for j in range(i+1, N):
            word2 = words[j]
            cnt += conf_alp()
            for key in match:
                match[key] = ''
            used.clear()
    return cnt

N = int(input())
words = [input() for _ in range(N)]
print(find_similar(N, words))