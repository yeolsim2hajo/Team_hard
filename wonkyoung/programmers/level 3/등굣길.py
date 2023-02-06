#230203
def solution(m, n, puddles):
    from math import comb
    answer = comb(m+n-2, m-1)
    for x, y in puddles:
        answer -= comb(x+y-2, x-1) * comb(m+n-(x+y), m-x)
    return answer