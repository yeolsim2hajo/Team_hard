#230114
# def solution(k, score):
#     min_number = score[0]
#     arr, answer = [min_number], [min_number]
#     length, cnt = len(score), 1
#     for i in range(1, length):
#         new_score = score[i]
#         if cnt < k:
#             for j in range(cnt-1, -1, -1):
#                 if arr[j] >= new_score:
#                     arr.insert(j + 1, new_score)
#                     break
#             else:
#                 arr.insert(0, new_score)
#             cnt += 1
#             min_number = arr[-1]
#         # print(i, new_score)
#         elif min_number < new_score:
#             # print(arr, new_score)
#             arr.pop()
#             cnt -= 1
#             if cnt < k:
#                 for j in range(cnt - 1, -1, -1):
#                     if arr[j] >= new_score:
#                         arr.insert(j + 1, new_score)
#                         break
#                 else:
#                     arr.insert(0, new_score)
#                 cnt += 1
#             min_number = arr[-1]
#         answer.append(min_number)
#     return answer

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
테스트 9 〉	통과 (0.05ms, 10.1MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.08ms, 10MB)
테스트 12 〉	통과 (0.52ms, 10MB)
테스트 13 〉	통과 (0.52ms, 10.1MB)
테스트 14 〉	통과 (0.52ms, 10MB)
테스트 15 〉	통과 (0.92ms, 10.1MB)
테스트 16 〉	통과 (0.80ms, 10.2MB)
테스트 17 〉	통과 (0.83ms, 10.2MB)
테스트 18 〉	통과 (0.77ms, 10.2MB)
테스트 19 〉	통과 (0.27ms, 10.3MB)
테스트 20 〉	통과 (0.18ms, 10.2MB)
테스트 21 〉	통과 (0.28ms, 10.1MB)
테스트 22 〉	통과 (0.28ms, 10.2MB)
테스트 23 〉	통과 (0.13ms, 10.2MB)
테스트 24 〉	통과 (0.15ms, 10.1MB)
테스트 25 〉	통과 (0.16ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10MB)
'''

# 함수화
# def solution(k, score):
#     min_number = score[0]
#     arr, answer = [min_number], [min_number]
#     length, cnt = len(score), 1
#
#     def find_min():
#         nonlocal cnt, min_number
#         for j in range(cnt - 1, -1, -1):
#             if arr[j] >= new_score:
#                 arr.insert(j + 1, new_score)
#                 break
#         else:
#             arr.insert(0, new_score)
#         cnt += 1
#         min_number = arr[-1]
#
#     for i in range(1, length):
#         new_score = score[i]
#         if cnt < k:
#             find_min()
#         elif min_number < new_score:
#             arr.pop()
#             cnt -= 1
#             find_min()
#         answer.append(min_number)
#     return answer
'''
테스트 1 〉	통과 (0.01ms, 9.95MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 9.97MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.06ms, 10.1MB)
테스트 12 〉	통과 (1.01ms, 10MB)
테스트 13 〉	통과 (0.59ms, 10.2MB)
테스트 14 〉	통과 (0.67ms, 10.1MB)
테스트 15 〉	통과 (1.43ms, 10.1MB)
테스트 16 〉	통과 (0.79ms, 10.1MB)
테스트 17 〉	통과 (1.24ms, 10.3MB)
테스트 18 〉	통과 (1.44ms, 10.1MB)
테스트 19 〉	통과 (0.24ms, 10.2MB)
테스트 20 〉	통과 (0.22ms, 10.1MB)
테스트 21 〉	통과 (0.29ms, 10.2MB)
테스트 22 〉	통과 (0.18ms, 10.3MB)
테스트 23 〉	통과 (0.26ms, 10.3MB)
테스트 24 〉	통과 (0.16ms, 10.2MB)
테스트 25 〉	통과 (0.16ms, 10.2MB)
테스트 26 〉	통과 (0.01ms, 10.1MB)
'''



# print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
# print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]	))