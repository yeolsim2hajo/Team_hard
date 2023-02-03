#230203
def solution(n):
    result = num = 1
    while True:
        if result == n:
            return num
        elif result > n:
            return num-1
        num += 1
        result *= num
