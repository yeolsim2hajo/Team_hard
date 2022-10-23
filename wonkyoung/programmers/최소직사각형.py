#221023
# def solution(sizes):
#     max_width = max_height = 0
#     for i in range(len(sizes)):
#         sizes[i].sort()
#         max_width = max(max_width, sizes[i][0])
#         max_height = max(max_height, sizes[i][1])
#     answer = max_width * max_height
#     return answer

'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.14ms, 10MB)
테스트 12 〉	통과 (0.14ms, 10.1MB)
테스트 13 〉	통과 (0.41ms, 10.2MB)
테스트 14 〉	통과 (0.79ms, 10.5MB)
테스트 15 〉	통과 (1.23ms, 10.3MB)
테스트 16 〉	통과 (2.19ms, 10.5MB)
테스트 17 〉	통과 (2.79ms, 10.8MB)
테스트 18 〉	통과 (3.20ms, 10.8MB)
테스트 19 〉	통과 (3.50ms, 11.3MB)
테스트 20 〉	통과 (3.98ms, 11.4MB)
'''

#zip 이용
def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort()
    sizes = list(zip(*sizes))
    max_width, max_height = max(sizes[0]), max(sizes[1])
    answer = max_width * max_height
    return answer
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.08ms, 10.3MB)
테스트 13 〉	통과 (0.21ms, 10.4MB)
테스트 14 〉	통과 (0.39ms, 10.6MB)
테스트 15 〉	통과 (1.23ms, 10.5MB)
테스트 16 〉	통과 (1.38ms, 11MB)
테스트 17 〉	통과 (1.63ms, 11.5MB)
테스트 18 〉	통과 (1.96ms, 11.6MB)
테스트 19 〉	통과 (3.65ms, 12.1MB)
테스트 20 〉	통과 (2.34ms, 12.2MB)
'''