#230315
N, M = map(int, input().split())
A = set(input().split())
twice = len(set(input().split()) & A) * 2
print(N+M-twice)