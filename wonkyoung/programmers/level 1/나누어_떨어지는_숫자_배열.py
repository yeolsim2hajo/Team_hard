def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor == 0:
            answer.append(num)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer
'''

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (3.29ms, 13.4MB)
테스트 7 〉	통과 (0.15ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.10ms, 10.2MB)
테스트 10 〉	통과 (0.08ms, 10.3MB)
테스트 11 〉	통과 (0.03ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.2MB)
테스트 13 〉	통과 (0.22ms, 10.2MB)
테스트 14 〉	통과 (0.10ms, 10.3MB)
테스트 15 〉	통과 (0.16ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.1MB)
'''

def solution(arr, divisor):
    answer = []
    arr.sort()
    num_set = set(range(divisor, arr[-1]+1, divisor))
    for num in arr:
        if num in num_set:
            answer.append(num)
    if not answer:
        answer.append(-1)
    return answer
'''
테스트 1 〉	통과 (0.70ms, 10.8MB)
테스트 2 〉	통과 (0.77ms, 10.7MB)
테스트 3 〉	통과 (3.40ms, 13.1MB)
테스트 4 〉	통과 (0.85ms, 10.8MB)
테스트 5 〉	통과 (27.82ms, 26.6MB)
테스트 6 〉	통과 (13.91ms, 13.3MB)
테스트 7 〉	통과 (0.63ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.40ms, 10.3MB)
테스트 10 〉	통과 (3.36ms, 13.2MB)
테스트 11 〉	통과 (1.10ms, 10.8MB)
테스트 12 〉	통과 (0.97ms, 10.9MB)
테스트 13 〉	통과 (0.64ms, 10.3MB)
테스트 14 〉	통과 (1.56ms, 10.8MB)
테스트 15 〉	통과 (1.28ms, 10.9MB)
테스트 16 〉	통과 (1.36ms, 10.8MB)
'''