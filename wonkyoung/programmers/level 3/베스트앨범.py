#230308
# heap
# def solution(genres, plays):
#     from heapq import heappush, heappop
#     answer = []
#     genre_cnt = {}
#     play_list = {}
#     length = len(genres)
#     keys = []
#     for i in range(length):
#         genre = genres[i]
#         play = plays[i]
#         if genre_cnt.get(genre):
#             genre_cnt[genre] += play
#             heappush(play_list[genre], (-play, i))
#         else:
#             genre_cnt[genre] = play
#             play_list[genre] = [(-play, i)]
#             keys.append(genre)
#     keys = sorted(keys, key= lambda genre: -genre_cnt[genre])
#     for genre in keys:
#         try:
#             for _ in range(2):
#                 answer.append(heappop(play_list[genre])[1])
#         except Exception:
#             pass
#     return answer
'''
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.06ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.10ms, 10.4MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.06ms, 10.3MB)
테스트 13 〉	통과 (0.08ms, 10.2MB)
테스트 14 〉	통과 (0.08ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
'''

# sort
# def solution(genres, plays):
#     answer = []
#     genre_cnt = {}
#     play_list = {}
#     length = len(genres)
#     keys = []
#     for i in range(length):
#         genre = genres[i]
#         play = plays[i]
#         if genre_cnt.get(genre):
#             genre_cnt[genre] += play
#             play_list[genre].append((- play, i))
#         else:
#             genre_cnt[genre] = play
#             play_list[genre] = [(- play, i)]
#             keys.append(genre)
#     keys = sorted(keys, key= lambda genre: -genre_cnt[genre])
#     for genre in keys:
#         play_list[genre].sort()
#         try:
#             for i in range(2):
#                 answer.append(play_list[genre][i][1])
#         except Exception:
#             pass
#     return answer
'''
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.09ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.06ms, 10.3MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
'''