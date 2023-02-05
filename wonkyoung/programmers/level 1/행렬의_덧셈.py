#230205
def solution(arr1, arr2):
    answer = []
    limit_i, limit_j = len(arr1), len(arr1[0])
    for i in range(limit_i):
        answer.append([])
        for j in range(limit_j):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.09ms, 10.2MB)
테스트 3 〉	통과 (0.29ms, 10.2MB)
테스트 4 〉	통과 (0.15ms, 10.4MB)
테스트 5 〉	통과 (0.12ms, 10.2MB)
테스트 6 〉	통과 (0.15ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (1.12ms, 10.8MB)
테스트 10 〉	통과 (0.86ms, 10.7MB)
테스트 11 〉	통과 (0.71ms, 10.5MB)
테스트 12 〉	통과 (1.36ms, 10.6MB)
테스트 13 〉	통과 (0.62ms, 10.6MB)
테스트 14 〉	통과 (0.66ms, 10.4MB)
테스트 15 〉	통과 (0.72ms, 10.5MB)
테스트 16 〉	통과 (0.69ms, 10.6MB)
테스트 17 〉	통과 (34.28ms, 22.8MB)
'''

# map 이용
def solution(arr1, arr2):
    answer = []
    limit_i, limit_j = len(arr1), len(arr1[0])
    for i in range(limit_i):
        answer.append(list(map(lambda x, y: x+y, arr1[i], arr2[i])))
    return answer
print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
'''

테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.30ms, 10.3MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.09ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.62ms, 10.8MB)
테스트 10 〉	통과 (0.87ms, 10.7MB)
테스트 11 〉	통과 (0.28ms, 10.4MB)
테스트 12 〉	통과 (0.39ms, 10.6MB)
테스트 13 〉	통과 (0.31ms, 10.6MB)
테스트 14 〉	통과 (0.37ms, 10.5MB)
테스트 15 〉	통과 (0.45ms, 10.6MB)
테스트 16 〉	통과 (0.40ms, 10.6MB)
테스트 17 〉	통과 (20.16ms, 22.9MB)
'''