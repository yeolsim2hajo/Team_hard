#230201
def solution(n):
    def find_root(n):
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            square = mid * mid
            if square == n:
                return mid
            elif square > n:
                end = mid - 1
            else:
                start = mid + 1
        return end

    root = find_root(n)
    answer = [1, n]
    position = 1
    for i in range(2, root+1):
        if n%i == 0:
            answer.insert(-position, n//i)
            answer.insert(position, i)
            position += 1
    if root * root == n:
        answer.remove(root)
    return answer
print(solution(1))
# print(solution(10000))
print(solution(100))
# print(solution(17))
'''
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.02ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.02ms, 9.97MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
'''