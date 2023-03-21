#230321
# from collections import deque
# document = list(map(str,input()))
# word = deque(map(str, input()))
# len_doc, len_word = len(document), len(word)
# doc_part = deque(document[:len_word - 1])
# i = cnt = 0
# while i <= len_doc - len_word:
#     doc_part.append(document[i+len_word - 1])
#     if doc_part == word:
#         i += len_word
#         cnt += 1
#         doc_part = deque(document[i:i+len_word - 1])
#     else:
#         i += 1
#         doc_part.popleft()
# print(cnt)


#
# def search():
#     from collections import deque
#     document = list(map(str, input()))
#     word = deque(map(str, input()))
#     len_doc, len_word = len(document), len(word)
#     doc_part = deque(document[:len_word - 1])
#     i = cnt = 0
#     while i <= len_doc - len_word:
#         doc_part.append(document[i+len_word - 1])
#         if doc_part == word:
#             i += len_word
#             cnt += 1
#             doc_part = deque(document[i:i+len_word - 1])
#         else:
#             i += 1
#             doc_part.popleft()
#     return cnt
# print(search())
