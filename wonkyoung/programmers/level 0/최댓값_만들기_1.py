#230207
# lambda, max
def solution(numbers):
    numbers.sort()
    return_multiple = lambda index: numbers[index] * numbers[index-1]
    answer =  max(return_multiple(1), return_multiple(-1))
    return answer


#
def solution(numbers):
    numbers.sort()
    answer = max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    return answer

# 원소 범위 적용
def solution(numbers):
    numbers.sort()
    return_multiple = lambda index: numbers[index] * numbers[index-1]
    answer = return_multiple(-1)
    return answer

#
def solution(numbers):
    numbers.sort()
    answer = numbers[-1]*numbers[-2]
    return answer