#220103
def solution(chicken):
    answer = 0
    while chicken >= 10:
        quot, remain = divmod(chicken, 10)
        answer += quot
        chicken = quot + remain
    return answer