#221110
N = int(input())
result = N * 100
papers = []
for _ in range(N):
    left, bottom = map(int, input().split())
    for left_range, bottom_range in papers:
        if left in left_range and bottom in bottom_range:
            left_length = list(left_range)
    papers.append((range(left, left+10), range(bottom-10, bottom)))
