#230125
def solution(numbers):
    answer = ''
    en_num = ['zero', 'one', 'two', 'three',
              'four', 'five', 'six', 'seven',
              'eight', 'nine']
    match = {en_num[i]:str(i) for i in range(10)}
    en_num = set(en_num)
    start, end = 0, 3
    length = len(numbers)
    while start < length:
        key = numbers[start:end]
        if key not in en_num:
            key += numbers[end]
            end += 1
            if key not in en_num:
                key += numbers[end]
                end += 1
        answer += match[key]
        start, end = end, end+3
    return int(answer)

solution("onetwothreefourfivesixseveneightnine")
'''
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
'''
def solution(numbers):
    answer = ''
    en_num = ['zero', 'one', 'two', 'three',
              'four', 'five', 'six', 'seven',
              'eight', 'nine']
    match = {en_num[i]:str(i) for i in range(10)}
    en_num = set(en_num)
    start, end = 0, 3
    length = len(numbers)
    while start < length:
        key = numbers[start:end]
        for _ in range(2):
            if key not in en_num:
                key += numbers[end]
                end += 1
            else:
                break
        answer += match[key]
        start, end = end, end+3
    return int(answer)
'''
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.5MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.04ms, 10.5MB)
'''

def solution(numbers):
    answer = ''
    en_num = ['zero', 'one', 'two', 'three',
              'four', 'five', 'six', 'seven',
              'eight', 'nine']
    match = {en_num[i]:str(i) for i in range(10)}
    en_num = set(en_num)
    start, end = 0, 3
    length = len(numbers)
    while start < length:
        for i in range(end, end+2):
            if numbers[start:i] in en_num:
                break
            else:
                end += 1
        answer += match[numbers[start:end]]
        start, end = end, end+3
    return int(answer)
'''
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.03ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.5MB)
테스트 9 〉	통과 (0.04ms, 10.3MB)
'''

def solution(numbers):
    answer = ''
    en_num = ['zero', 'one', 'two', 'three',
              'four', 'five', 'six', 'seven',
              'eight', 'nine']
    match = {en_num[i]:str(i) for i in range(10)}
    start, end = 0, 3
    length = len(numbers)
    while start < length:
        key = numbers[start:end]
        for _ in range(2):
            if match.get(key):
                break
            else:
                key += numbers[end]
                end += 1
        answer += match[key]
        start, end = end, end+3
    return int(answer)
'''
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.4MB)
'''
def solution(numbers):
    answer = 0
    en_num = ['zero', 'one', 'two', 'three',
              'four', 'five', 'six', 'seven',
              'eight', 'nine']
    match = {en_num[i]:i for i in range(10)}
    en_num = set(en_num)
    length = len(numbers)
    start, end = 0, 3
    while start < length:
        key = numbers[start:end]
        for _ in range(2):
            if key in en_num:
                break
            else:
                key += numbers[end]
                end += 1
        answer *= 10
        answer += match[key]
        start, end = end, end+3

    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
'''