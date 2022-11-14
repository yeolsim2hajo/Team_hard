#221114
def main():
    N, M = map(int, input().split())
    if not (1 <= M <= 3) or not (1 <= N <= 100):
        return ['INPUT ERROR!']
    start, end, step, space = [(), (1, N+1, 1, 0), (N, 0, -1, 0), (1, 2*N, 2, 1)][M]
    result = []
    for i in range(start, end, step):
        result.append(' ' * space * (N-1-i//2) + '*' * i)
    return result
print(*main(), sep='\n')
