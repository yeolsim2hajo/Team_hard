#230216
def solution(sides):
    # 가장 긴 변 = sides[1] => sides[1] - sides[0] < x <= sides[1]
    # => sides[0]
    # total > 가장 긴 변 > sides[1]
    # => sides[0]-1
    answer = 2*min(sides) - 1
    return answer
'''
테스트 1 〉	통과 (0.00ms, 9.97MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.00ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.00ms, 9.93MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
'''