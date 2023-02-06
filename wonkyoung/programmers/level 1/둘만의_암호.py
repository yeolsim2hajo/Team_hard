#230203
# 실패
# def solution(s, skip, index):
#     match = {}
#     check = [1] * 26
#     for alp in skip:
#         check[ord(alp)-97] = 0
#     for i in range(26):
#         start = 97+i
#         alp = chr(start)
#         if alp not in skip:
#             end = 97+i+index
#             if end < 97+26:
#                 end += check[start:end+1].count(0)
#             else:
#
#
#             after = chr(after_i) if after_i <= 97+25 else chr(after_i-26)
#
#     answer = ''
#     return answer

#230206
# def solution(s, skip, index):
#     skip = set(map(str, skip))
#     alphabet = [chr(97+i) for i in range(26)]
#     conv = {}
#     for i in range(26):
#         now, cnt = i, 0
#         while cnt <= index:
#             if now < 26:
#                 if alphabet[now] not in skip:
#                     cnt += 1
#                 now += 1
#             else:
#                 now -= 26
#         conv[alphabet[i]] = alphabet[now-1]
#     answer = ''
#     for alp in s:
#         answer += conv[alp]
#     return answer
'''
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.11ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.11ms, 10.3MB)
테스트 12 〉	통과 (0.03ms, 10.4MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.05ms, 10.3MB)
테스트 16 〉	통과 (0.14ms, 10.4MB)
테스트 17 〉	통과 (0.10ms, 10.1MB)
테스트 18 〉	통과 (0.09ms, 10.4MB)
테스트 19 〉	통과 (0.10ms, 10.2MB)
'''

# set 이용
def solution(s, skip, index):
    skip = set(map(str, skip))
    alphabet = sorted(set(chr(97+i) for i in range(26)) - skip)
    conv, answer = {}, ''
    length = len(alphabet)
    for i in range(length):
        now = i+index
        while now >= length:
            now -= length
        conv[alphabet[i]] = alphabet[now]
    for alp in s:
        answer += conv[alp]
    return answer
print(solution("aukks",	"wbqd",	5))
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.02ms, 10.2MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.2MB)
테스트 17 〉	통과 (0.02ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.3MB)
테스트 19 〉	통과 (0.02ms, 10.2MB)
'''




