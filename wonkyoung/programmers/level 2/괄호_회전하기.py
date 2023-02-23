def solution(s):
    from collections import deque
    s = deque(map(str, s))
    len_s = len(s)
    answer = 0
    stack = []
    open = {'[', '(', '{'}
    match = {'[':']', '(':')', '{':'}'}
    if len_s%2 == 0:
        for _ in range(len_s):
            for element in s:
                if element in open:
                    stack.append(element)
                elif stack:
                    last = stack.pop()
                    if match[last] != element:
                        break
                else:
                    break
            else:
                if not stack:
                    answer += 1
            first = s.popleft()
            s.append(first)
    return answer
'''
테스트 1 〉	통과 (4.88ms, 10.2MB)
테스트 2 〉	통과 (2.49ms, 10.3MB)
테스트 3 〉	통과 (2.48ms, 10.3MB)
테스트 4 〉	통과 (3.60ms, 10.1MB)
테스트 5 〉	통과 (13.14ms, 10.4MB)
테스트 6 〉	통과 (5.17ms, 10.4MB)
테스트 7 〉	통과 (7.14ms, 10.3MB)
테스트 8 〉	통과 (9.77ms, 10.3MB)
테스트 9 〉	통과 (19.20ms, 10.3MB)
테스트 10 〉	통과 (29.47ms, 10.4MB)
테스트 11 〉	통과 (45.06ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
'''