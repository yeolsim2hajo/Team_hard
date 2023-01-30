#230130
def solution(n):
    num_list = set(range(3, n+1, 2))
    num_list.add(2)
    for num in range(3, n+1, 2):
        multiple_num = num * 3
        while multiple_num <= n:
            num_list.discard(multiple_num)
            multiple_num += 2 * num
    return len(num_list)
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.3MB)
테스트 4 〉	통과 (0.15ms, 10.2MB)
테스트 5 〉	통과 (0.19ms, 10.3MB)
테스트 6 〉	통과 (3.71ms, 10.5MB)
테스트 7 〉	통과 (0.71ms, 10.2MB)
테스트 8 〉	통과 (1.39ms, 10.3MB)
테스트 9 〉	통과 (3.90ms, 10.4MB)
테스트 10 〉	통과 (111.83ms, 18.3MB)
테스트 11 〉	통과 (349.64ms, 43.8MB)
테스트 12 〉	통과 (113.71ms, 18.8MB)
효율성  테스트
테스트 1 〉	통과 (381.56ms, 43.8MB)
테스트 2 〉	통과 (368.66ms, 43.7MB)
테스트 3 〉	통과 (342.45ms, 43.8MB)
테스트 4 〉	통과 (370.60ms, 43.7MB)
'''

def solution(n):
    num_list = set(range(3, n+1, 2))
    num_list.add(2)
    for num in range(3, n+1, 2):
        multiple_num = num * 3
        while multiple_num <= n:
            if multiple_num in num_list:
                num_list.remove(multiple_num)
            multiple_num += 2 * num
    return len(num_list)
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.15ms, 10.2MB)
테스트 5 〉	통과 (0.10ms, 10.2MB)
테스트 6 〉	통과 (1.63ms, 10.4MB)
테스트 7 〉	통과 (0.40ms, 10.4MB)
테스트 8 〉	통과 (1.28ms, 10.3MB)
테스트 9 〉	통과 (2.00ms, 10.3MB)
테스트 10 〉	통과 (82.68ms, 18.3MB)
테스트 11 〉	통과 (307.43ms, 43.9MB)
테스트 12 〉	통과 (95.43ms, 18.9MB)
효율성  테스트
테스트 1 〉	통과 (301.02ms, 43.8MB)
테스트 2 〉	통과 (326.36ms, 43.7MB)
테스트 3 〉	통과 (344.46ms, 43.9MB)
테스트 4 〉	통과 (331.11ms, 43.7MB)
'''

def solution(n):
    three_to_n = range(3, n+1, 2)
    num_list = set(three_to_n)
    num_list.add(2)
    for num in three_to_n:
        multiple_num = num * 3
        while multiple_num <= n:
            if multiple_num in num_list:
                num_list.remove(multiple_num)
            multiple_num += 2 * num
    return len(num_list)
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.24ms, 10.2MB)
테스트 5 〉	통과 (0.18ms, 10.2MB)
테스트 6 〉	통과 (1.61ms, 10.4MB)
테스트 7 〉	통과 (0.40ms, 10.2MB)
테스트 8 〉	통과 (2.36ms, 10.4MB)
테스트 9 〉	통과 (1.97ms, 10.4MB)
테스트 10 〉	통과 (81.20ms, 18.4MB)
테스트 11 〉	통과 (346.30ms, 43.9MB)
테스트 12 〉	통과 (98.41ms, 18.8MB)
효율성  테스트
테스트 1 〉	통과 (303.93ms, 43.9MB)
테스트 2 〉	통과 (326.26ms, 43.8MB)
테스트 3 〉	통과 (340.45ms, 43.8MB)
테스트 4 〉	통과 (332.59ms, 43.8MB)
'''
