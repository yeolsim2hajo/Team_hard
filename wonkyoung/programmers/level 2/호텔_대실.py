#230314
# def solution(book_time):
#     length = len(book_time)
#     def to_int(str_time):
#         answer = int(str_time[:2]) * 60 + int(str_time[-2:])
#         return answer
#     for i in range(length):
#         book_time[i][0] = to_int(book_time[i][0])
#         book_time[i][1] = to_int(book_time[i][1])
#     book_time.sort()
#     room = 1
#     end_time = [book_time[0][1] + 10]
#     for i in range(1, length):
#         start, end = book_time[i]
#         for j in range(room):
#             if end_time[j] <= start:
#                 end_time[j] = end + 10
#                 break
#         else:
#             end_time.append(end + 10)
#             room += 1
#     return room
'''
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.74ms, 10.3MB)
테스트 3 〉	통과 (6.10ms, 10.5MB)
테스트 4 〉	통과 (4.66ms, 10.5MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (4.88ms, 10.5MB)
테스트 7 〉	통과 (5.74ms, 10.4MB)
테스트 8 〉	통과 (1.26ms, 10.5MB)
테스트 9 〉	통과 (0.73ms, 10.4MB)
테스트 10 〉	통과 (3.11ms, 10.4MB)
테스트 11 〉	통과 (9.17ms, 10.6MB)
테스트 12 〉	통과 (6.77ms, 10.5MB)
테스트 13 〉	통과 (0.47ms, 10.3MB)
테스트 14 〉	통과 (10.61ms, 10.5MB)
테스트 15 〉	통과 (12.46ms, 10.4MB)
테스트 16 〉	통과 (1.23ms, 10.4MB)
테스트 17 〉	통과 (7.37ms, 10.5MB)
테스트 18 〉	통과 (3.29ms, 10.5MB)
테스트 19 〉	통과 (21.77ms, 10.6MB)
'''

#
# def solution(book_time):
#     from heapq import heappush, heappop
#     length = len(book_time)
#     def to_int(str_time):
#         answer = int(str_time[:2]) * 60 + int(str_time[-2:])
#         return answer
#     for i in range(length):
#         book_time[i][0] = to_int(book_time[i][0])
#         book_time[i][1] = to_int(book_time[i][1])
#     book_time.sort()
#     room = 1
#     end_time = [book_time[0][1] + 10]
#     for i in range(1, length):
#         start, end = book_time[i]
#         if end_time[0] <= start:
#             heappop(end_time)
#             room -= 1
#         heappush(end_time, end+10)
#         room += 1
#     return room
'''
테스트 1 〉	통과 (0.07ms, 10.4MB)
테스트 2 〉	통과 (0.27ms, 10.4MB)
테스트 3 〉	통과 (1.30ms, 10.5MB)
테스트 4 〉	통과 (0.78ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (1.94ms, 10.4MB)
테스트 7 〉	통과 (2.03ms, 10.5MB)
테스트 8 〉	통과 (0.58ms, 10.4MB)
테스트 9 〉	통과 (0.73ms, 10.4MB)
테스트 10 〉	통과 (1.44ms, 10.4MB)
테스트 11 〉	통과 (2.69ms, 10.5MB)
테스트 12 〉	통과 (1.37ms, 10.4MB)
테스트 13 〉	통과 (0.26ms, 10.3MB)
테스트 14 〉	통과 (2.08ms, 10.5MB)
테스트 15 〉	통과 (2.54ms, 10.5MB)
테스트 16 〉	통과 (0.51ms, 10.4MB)
테스트 17 〉	통과 (2.76ms, 10.7MB)
테스트 18 〉	통과 (1.62ms, 10.4MB)
테스트 19 〉	통과 (1.20ms, 10.6MB)
'''

#
def solution(book_time):
    from heapq import heappush, heappop
    def conv_time():
        def to_int(str_time):
            answer = int(str_time[:2]) * 60 + int(str_time[-2:])
            return answer
        for i in range(length):
            book_time[i][0] = to_int(book_time[i][0])
            book_time[i][1] = to_int(book_time[i][1])
        book_time.sort()

    length = len(book_time)
    conv_time()
    room = 1
    end_time = [book_time[0][1] + 10]
    for i in range(1, length):
        start, end = book_time[i]
        if end_time[0] <= start:
            heappop(end_time)
            room -= 1
        heappush(end_time, end+10)
        room += 1
    return room
'''
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.28ms, 10.3MB)
테스트 3 〉	통과 (1.27ms, 10.3MB)
테스트 4 〉	통과 (0.71ms, 10.6MB)
테스트 5 〉	통과 (0.03ms, 10.5MB)
테스트 6 〉	통과 (1.12ms, 10.4MB)
테스트 7 〉	통과 (1.95ms, 10.4MB)
테스트 8 〉	통과 (0.95ms, 10.4MB)
테스트 9 〉	통과 (0.34ms, 10.3MB)
테스트 10 〉	통과 (0.90ms, 10.5MB)
테스트 11 〉	통과 (2.85ms, 10.5MB)
테스트 12 〉	통과 (2.08ms, 10.4MB)
테스트 13 〉	통과 (0.26ms, 10.2MB)
테스트 14 〉	통과 (1.15ms, 10.4MB)
테스트 15 〉	통과 (1.40ms, 10.5MB)
테스트 16 〉	통과 (0.99ms, 10.5MB)
테스트 17 〉	통과 (1.48ms, 10.6MB)
테스트 18 〉	통과 (0.91ms, 10.2MB)
테스트 19 〉	통과 (1.19ms, 10.6MB)
'''