#230128
def solution(numbers):
    numbers.sort()
    answer = max(numbers[0] * numbers[1], numbers[-2] * numbers[-1])
    return answer