#230208
def solution(num, total):
    total_quot, num_quot = total//num, num//2
    start, end = total_quot - num_quot, total_quot + num_quot + 1
    if num%2 == 0:
        start = total_quot - num_quot + 1
    return list(range(start, end))