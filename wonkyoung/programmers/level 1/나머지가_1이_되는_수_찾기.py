#230113
def solution(n):
    if n%2:
        return 2
    else:
        for number in range(3, n, 2):
            if n%number == 1:
                return number