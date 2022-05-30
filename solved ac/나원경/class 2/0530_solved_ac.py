#1654 랜선 자르기
K, N = map(int, input().split())
lines = []
max_val = 0
for _ in range(K):
    lines.append(int(input()))
    max_val = lines[-1] if max_val < lines[-1] else max_val
def find_max():
    start = 1
    end = max_val
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in range(K):
            cnt += lines[i] // mid
        if cnt >= N:
            start = mid + 1
        else:
            end = mid - 1
    if end == 0:
        print(start)
    else:
        start_cnt = end_cnt = 0
        for i in range(K):
            start_cnt += lines[i] // start
            end_cnt += lines[i] // end
        if start_cnt >= N:
            print(start)
        else:
            print(end)

find_max()

