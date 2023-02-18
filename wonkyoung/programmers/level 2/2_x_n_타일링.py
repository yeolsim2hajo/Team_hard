#230218
# def solution(n):
#     from collections import deque
#     if n < 4:
#         return n
#     placement = deque([{'111', '12', '21'}, {'11', '2'}])
#     less_than_three = [{'1'}, {'11', '2'}]
#     for _ in range(4, n+1):
#         new_set = set()
#         for i in range(2):
#            for each in placement[i]:
#                for number in less_than_three[i]:
#                    new_set.add(each+number)
#                    new_set.add(number+each)
#         placement.pop()
#         placement.appendleft(new_set)
#     print(placement[0])
#     return len(placement[0])
#
def solution(n):
    from collections import deque
    if n < 4:
        return n
    cases = deque(range(1, 4))
    # n-3 / n-2 / n-1
    for i in range(4, n+1):
        '''
        5
        111/11
        21/11
        111/2
        n-2개 순열*2개 순열
        11/2/1
        n-1/1
        n-3개 순열
        '''
        case = cases[0] + cases[1] * 2
        cases.popleft()
        cases.append(case)
    return cases[-1]%(int(1e9) + 7)
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(1008))
'''
테스트 1 〉	통과 (2.89ms, 10.1MB)
테스트 2 〉	통과 (0.29ms, 10.2MB)
테스트 3 〉	통과 (1.60ms, 10.1MB)
테스트 4 〉	통과 (3.79ms, 10.1MB)
테스트 5 〉	통과 (0.22ms, 10.1MB)
테스트 6 〉	통과 (3.14ms, 10.3MB)
테스트 7 〉	통과 (0.24ms, 10.2MB)
테스트 8 〉	통과 (1.78ms, 10.3MB)
테스트 9 〉	통과 (1.66ms, 9.99MB)
테스트 10 〉	통과 (3.39ms, 10MB)
테스트 11 〉	통과 (1.20ms, 10.3MB)
테스트 12 〉	통과 (0.51ms, 10.3MB)
테스트 13 〉	통과 (0.43ms, 10.1MB)
테스트 14 〉	통과 (1.14ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (11.47ms, 10.2MB)
테스트 2 〉	통과 (24.24ms, 10.1MB)
테스트 3 〉	통과 (11.30ms, 10.1MB)
테스트 4 〉	통과 (8.02ms, 10.1MB)
테스트 5 〉	통과 (35.04ms, 10.2MB)
테스트 6 〉	통과 (63.42ms, 10.3MB)
'''