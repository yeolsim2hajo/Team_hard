#230222
def solution(n, numlist):
    answer = [num for num in numlist if num%n == 0]
    return answer