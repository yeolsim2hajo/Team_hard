#230121
def solution(a, b):
    weekday = ['SUN', 'MON','TUE', 'WED', 'THU', 'FRI', 'SAT']
    index = 5
    months = [0] * 12
    thirty = {4, 6, 9, 11}
    months[1:3] = [31, 60]
    for i in range(3, 12):
        months[i] += months[i-1]
        if i in thirty:
            months[i] += 30
        else:
            months[i] += 31
    total = months[a-1] + b-1
    index = (total%7 + index)%7
    return weekday[index]
'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.3MB)
'''
def solution(a, b):
    weekday = ['SUN', 'MON','TUE', 'WED', 'THU', 'FRI', 'SAT']
    index = 5
    months = [0] * 12
    months[2] = -1
    thirty = {2, 4, 6, 9, 11}
    for i in range(1, 12):
        months[i] += months[i-1]
        if i in thirty:
            months[i] += 30
        else:
            months[i] += 31
    total = months[a-1] + b-1
    index = (total%7 + index)%7
    return weekday[index]
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''