#230301
# def solution(str1, str2):
#     str1 = str1.lower()
#     str2 = str2.lower()
#     intersection = union = 0
#     cnt = {}
#     for i in range(len(str1)-1):
#         alp = str1[i:i+2]
#         if not alp.isalpha():
#             continue
#         elif cnt.get(alp):
#             cnt[alp] += 1
#         else:
#             cnt[alp] = 1
#         union += 1
#
#     for i in range(len(str2) - 1):
#         alp = str2[i:i + 2]
#         if not alp.isalpha():
#             continue
#         elif cnt.get(alp):
#             cnt[alp] -= 1
#             intersection += 1
#         else:
#             union += 1
#     answer = 65536 if union == 0 else (intersection * 65536)//union
#     return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.56ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.4MB)
테스트 9 〉	통과 (0.06ms, 10.4MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
테스트 11 〉	통과 (0.25ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
'''

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    intersection = union = 0
    cnt = {}
    for i in range(len(str1)-1):
        alp = str1[i:i+2]
        if alp.isalpha():
            if cnt.get(alp):
                cnt[alp] += 1
            else:
                cnt[alp] = 1
            union += 1

    for i in range(len(str2) - 1):
        alp = str2[i:i + 2]
        if alp.isalpha():
            if cnt.get(alp):
                cnt[alp] -= 1
                intersection += 1
            else:
                union += 1
    answer = 65536 if union == 0 else (intersection * 65536)//union
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.53ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
테스트 10 〉	통과 (0.07ms, 10.3MB)
테스트 11 〉	통과 (0.18ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.03ms, 10.3MB)
'''