#230103
def solution(x):
    str_x = str(x)
    total = 0
    for num in str_x:
        total += int(num)
    answer = x % total == 0
    return answer