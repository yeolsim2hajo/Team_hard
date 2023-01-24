def solution(n):
    answer = sorted(map(str, str(n)), reverse=True)
    return int(''.join(answer))