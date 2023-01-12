#220920
def solution(name):
    answer = 0
    alphabet = {}
    for i in range(26):
        alphabet[chr(65+i)] = min(i, 26-i)
    length = len(name)
    min_cnt = 0
    a_cnt = 0

    for i in range(length):
        key = name[i]
        if key == 'A':
            a_cnt += 1
        min_cnt += alphabet[key]
    min_cnt -= a_cnt + 1
    return answer




# 그 전 - 맞지 않는 코드
# def solution(name):
#     answer = 0
#     alphabet = {}
#     for i in range(1,26):
#         if i < 13:
#             alphabet[chr(65+i)] = i
#         else:
#             alphabet[chr(65 + i)] = 26-i
#     cnt = 0
#     position_a = []
#     for i in range(len(name)):
#         alp = name[i]
#         if alp != 'A':
#             answer += alphabet[alp]
#             if cnt:
#                 position_a.append((i-cnt,cnt))
#                 cnt = 0
#         else:
#             cnt += 1
#     length = len(name)
#     min_val = length - 1
#     if position_a:
#         for start,cnt in position_a:
#             if start in {0,1}:
#                 min_val = min(length - cnt - start, min_val)
#             else:
#                 min_val = min(length + start - cnt - 1, min_val)
#     answer += min_val
#     return answer