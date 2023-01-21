#230121
def solution(X, Y):
    answer = []
    numbers = {str(i):0 for i in range(10)}
    for num in X:
        numbers[num] += 1
    for num in Y:
        if numbers[num]:
            numbers[num] -= 1
            answer.append(num)
    if answer:
        answer.sort(reverse=True)
        if answer[0] == '0':
            return '0'
        return ''.join(answer)
    return '-1'
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 9.92MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.31ms, 10.2MB)
테스트 7 〉	통과 (0.10ms, 10.1MB)
테스트 8 〉	통과 (0.26ms, 10.2MB)
테스트 9 〉	통과 (0.11ms, 10.3MB)
테스트 10 〉	통과 (0.13ms, 10.3MB)
테스트 11 〉	통과 (1197.05ms, 56.1MB)
테스트 12 〉	통과 (995.03ms, 56.1MB)
테스트 13 〉	통과 (1143.75ms, 56.3MB)
테스트 14 〉	통과 (1099.15ms, 56.1MB)
테스트 15 〉	통과 (988.67ms, 56.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.2MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
'''
def solution(X, Y):
    answer = []
    numbers = {str(i):0 for i in range(10)}
    if len(X) < len(Y):
        X, Y = Y, X
    for num in X:
        numbers[num] += 1
    for num in Y:
        if numbers[num]:
            numbers[num] -= 1
            answer.append(num)
    if answer:
        answer.sort(reverse=True)
        if answer[0] == '0':
            return '0'
        return ''.join(answer)
    return '-1'
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.17ms, 10.1MB)
테스트 7 〉	통과 (0.10ms, 10.2MB)
테스트 8 〉	통과 (0.28ms, 10.2MB)
테스트 9 〉	통과 (0.10ms, 9.99MB)
테스트 10 〉	통과 (0.13ms, 10.2MB)
테스트 11 〉	통과 (1132.18ms, 56.2MB)
테스트 12 〉	통과 (1073.66ms, 56.2MB)
테스트 13 〉	통과 (1093.22ms, 56.3MB)
테스트 14 〉	통과 (975.98ms, 56.2MB)
테스트 15 〉	통과 (979.83ms, 56MB)
테스트 16 〉	통과 (0.01ms, 10.2MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.4MB)
'''
def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        str_i = str(i)
        cnt_x, cnt_y = X.count(str_i), Y.count(str_i)
        answer += str_i * min(cnt_x, cnt_y)
    if not answer:
        return '-1'
    if answer[0] == '0':
        return '0'
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.03ms, 10.2MB)
테스트 8 〉	통과 (0.03ms, 10.1MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (81.06ms, 27.5MB)
테스트 12 〉	통과 (79.89ms, 27.6MB)
테스트 13 〉	통과 (79.90ms, 27.6MB)
테스트 14 〉	통과 (80.37ms, 27.7MB)
테스트 15 〉	통과 (79.59ms, 27.6MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.01ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
'''