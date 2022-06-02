#2805 나무 자르기
N, M = map(int, input().split())
heights = list(map(int,input().split()))
start = 0
end = max(heights)
max_height = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for height in heights:
        if height > mid:
            total += height - mid
    if total == M:
        max_height = mid
        break
    elif total > M:
        start = mid + 1
    else:
        end = mid - 1
else:
    max_height = end
print(max_height)