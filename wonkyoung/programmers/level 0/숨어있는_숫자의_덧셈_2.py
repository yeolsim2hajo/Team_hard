#230128
def solution(my_string):
    answer = start = 0
    length = len(my_string)
    while start < length:
        if my_string[start].isdigit():
            end = start+1
            for end in range(start+1, length):
                if my_string[end].isdigit():
                    end += 1
                else:
                    break
            answer += int(my_string[start:end])
            start = end
        else:
            start += 1
    return answer
'''
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.03ms, 10MB)
테스트 10 〉	통과 (0.02ms, 10.1MB)
'''